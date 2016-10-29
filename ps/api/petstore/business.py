from ps.database import db


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


def update_user_name(user_id, data):
    from ps.database.models import User
    user= User.query.filter(User.id == user_id).one()
    user.name = data.get('name')
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    from ps.database.models import User
    category = User.query.filter(User.id == user_id).one()
    db.session.delete(category)
    db.session.commit()
