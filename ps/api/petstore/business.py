import datetime
from ps.app import db
from ps.database.models import UserStatus
from flask_restplus import abort


def create_pet(data):
    from ps.database.models import Pet
    name = data.get('name')
    cost = data.get('cost', 20)
    pet_type = data.get('type')
    status = "for sale"
    pet = Pet(
        name=name,
        pet_status=status,
        cost=cost,
        type=pet_type,
        added_by=1,
        added_at=datetime.datetime.now()
    )
    db.session.add(pet)
    db.session.commit()


def update_pet(pet_id, data):
    """
    Update a pet
    One may only update the name and cost, not status
    :param pet_id:
    :param data:
    :return:
    """
    from ps.database.models import Pet
    pet = Pet.query.filter(Pet.id == pet_id).one()
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
    from ps.database.models import Pet
    pet = Pet.query.filter(Pet.id == pet_id).one()
    pet.status = status
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
    from ps.database.models import User
    role = "customer"

    # intended bug -- can overwrite a user id by passing one in!
    if 'id' in data:
        id = data.get('id')
    else:
        id = None
    email = data.get('email')
    password = data.get('password')
    bank_account_balance_dollars = data.get('bank_account_balance_dollars', 200)
    status = 'registered'

    try:
        existing_by_email = User.query.filter(User.email == email).one()
    except:
        # hella ugly, but drops in here when user doesn't already exist.
        user = User(email=email, role=role, password=password,
                    bank_account_balance_dollars=bank_account_balance_dollars,
                    status=status)

        if id:
            user.id = id

        db.session.add(user)
        db.session.commit()


def update_user(user_id, data):
    from ps.database.models import User
    user= User.query.filter(User.id == user_id).one()

    em = data.get('email')
    if em:
        user.email = em

    status = data.get('status')
    if status:
        try:
            st = UserStatus.query.filter(UserStatus.status == status).one()
            user.status = st.id
        except:
            all_statuses = [s.status for s in UserStatus.query.all()]
            abort(422, message=\
            "No such status: {0}.  Valid statuses are: {1}".format(
                    status,
                    ','.join(all_statuses)
                )
            )

    pw = data.get('password')
    if pw:
        user.password = pw

    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    from ps.database.models import User
    user = User.query.filter(User.id == user_id).one()
    user.status = 'unregistered'
    db.session.add(user)
    db.session.commit()
