import ps
import datetime
from ps.app import db
from flask_restplus import abort


def create_pet(data):
    name = data.get('name')
    cost = data.get('cost', 20)
    pet_type = data.get('pet_type')
    status = "for sale"
    pet = ps.database.models.Pet(name=name, pet_status=status,
              cost=cost, pet_type=pet_type,
              last_modified_by=1, added_at = datetime.datetime.now()
              )
    db.session.add(pet)
    db.session.commit()
    return pet.to_json()


def update_pet(pet_id, data):
    """
    Update a pet
    One may only update the name and cost, not status
    :param pet_id:
    :param data:
    :return:
    """
    pet = ps.database.models.Pet.query.filter(ps.database.models.Pet.id ==
                                              pet_id).one()
    pet.name = data.get('name')
    pet.cost = data.get('cost')
    db.session.add(pet)
    db.session.commit()


def update_pet_status(pet_id, status):
    """
    soft-delete of a pet
    :param pet_id:
    :return:
    """
    pet = ps.database.models.Pet.query.filter(
        ps.database.models.Pet.id == pet_id
    ).one()
    pet.pet_status = status
    db.session.add(pet)
    db.session.commit()


def sell_pet(pet_id):
    update_pet_status(pet_id, 'sold')


def delete_pet(pet_id):
    update_pet_status(pet_id, 'deleted')


def create_user(data):
    """
    Users are either 'admin' or 'customer'

    :param data:
    :return:
    """
    role = "customer"

    # intended bug -- can overwrite a user id by passing one in!
    if 'id' in data:
        id = data.get('id')
    else:
        id = None
    username = data.get('username')
    password = data.get('password')
    bank_account_balance_dollars = data.get('bank_account_balance_dollars', 200)
    status = 'registered'

    try:
        existing_by_username = ps.database.models.User.query.filter(
            ps.database.models.User.username == username).one()
        print "already exists -- gonna abort"
        abort(400, "User with that username already exists")
    except Exception as e:
        # hella ugly, but drops in here when user doesn't already exist.
        user = ps.database.models.User(
            username=username, role=role,
            password=password,
            bank_account_balance_dollars=bank_account_balance_dollars,
            status=status
        )

        if id:
            user.id = id

        db.session.add(user)
        db.session.commit()

        return user.to_json()


def update_user(user_id, data):
    user = ps.database.models.User.query.filter(ps.database.models.User.id == user_id).one()

    em = data.get('username')
    if em:
        user.username = em

    status = data.get('status')
    if status:
        if status not in ['sold', 'for sale', 'removed']:
            abort(
                422,
                message="Valid statuses are 'sold', 'for sale' or 'removed'"
            )
            user.status = status

    pw = data.get('password')
    if pw:
        user.password = pw

    db.session.add(user)
    db.session.commit()

def get_orders():
    orders = ps.database.models.Order.query.all()
    if orders:
        return orders, 200
    else:
        return [], 200

def delete_order(order_id):
    order = ps.database.models.Order.query.filter(ps.database.models.Order.id == order_id).one()
    order.status = "deleted"
    db.session.add(order)
    db.session.commit()


def delete_user(user_id):
    user = ps.database.models.User.query.filter(
        ps.database.models.User.id == user_id
    ).one()
    user.status = "unregistered"
    db.session.add(user)
    db.session.commit()

def add_order(buyer_id, pet_id):
    order = ps.database.models.Order(
        pet_id=pet_id,
        user_id=buyer_id
    )

    buyer = ps.database.models.User(id=buyer_id),
    pet = ps.database.models.Pet(id=pet_id),

    if buyer.bank_account_balance_dollars < pet.cost:
        abort(422, 'Insufficient funds')
    newbal = buyer.bank_account_balance_dollars - pet.cost

    # BUG:
    # we debit the buyer's account and set the pet to sold in two
    # transactions which means two buyers could totally buy the same pet.

    # update buyer's bank account and create the order
    buyer.bank_account_balance_dollars = newbal
    db.sesion.add(buyer)
    db.session.add(order)
    db.session.commit()
    datetime.time.sleep(300)

    # update pet status
    pet.pet_status = 'sold'
    db.session.add(pet)
    db.session.commit()
    return order.to_json()
