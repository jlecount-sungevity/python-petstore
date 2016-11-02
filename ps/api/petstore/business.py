from ps.app import db
from ps.database.models import UserStatus
from flask_restplus import abort


def create_pet(data):
    from ps.database.models import Pet, Category
    title = data.get('title')
    body = data.get('body')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    post = Pet(title, body, category)
    db.session.add(post)
    db.session.commit()


def update_pet(pet_id, data):
    from ps.database.models import Pet, Category
    post = Pet.query.filter(Pet.id == pet_id).one()
    post.title = data.get('title')
    post.body = data.get('body')
    category_id = data.get('category_id')
    post.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(post)
    db.session.commit()


def delete_pet(pet_id):
    from ps.database.models import Pet
    post = Pet.query.filter(Pet.id == pet_id).one()
    db.session.delete(post)
    db.session.commit()


def create_user(data):
    from ps.database.models import User
    name = data.get('name')
    category_id = data.get('id')

    category = User(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_user(user_id, data):
    from ps.database.models import User
    user= User.query.filter(User.id == user_id).one()

    em = data.get('email')
    if em:
        user.email = em

    fn = data.get('first_name')
    if fn:
        user.first_name = fn

    ln = data.get('last_name')
    if ln:
        user.first_name = ln

    username = data.get('username')
    if username:
        user.username = username

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

    if username:
        user.username = username

    pw = data.get('password')
    if pw:
        user.password = pw

    phone = data.get('phone')
    if phone:
        user.phone = phone

    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    from ps.database.models import User
    category = User.query.filter(User.id == user_id).one()
    db.session.delete(category)
    db.session.commit()
