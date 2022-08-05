""" CRUD operations -- Create Read Update Delete """

from model import db, User, Park, UserTopPark, UserNote, connect_to_db


def create_user(username, email, password):
    """ Create and return a new user. """

    user = User(username=username, email=email, password=password)

    #add and commit to db
    db.session.add(user)
    db.session.commit()

    return user


def create_park(external_id, park_code, park_name):
    """ Create and return a new park """

    park = Park(external_id=external_id, park_code=park_code, park_name=park_name)

    db.session.add(park)
    db.session.commit()

    return park


def create_user_top_park(user_id, park_id):
    """ Create and return a new user top park. """

    user_top_park = UserTopPark(user_id=user_id, park_id=park_id)

    db.session.add(user_top_park)
    db.session.commit()

    return user_top_park


def create_user_note(user_id, park_id, note):
    """ Create and return a new user note. """

    user_note = UserNote(user_id=user_id, park_id=park_id, note=note)

    db.session.add(user_note)
    db.session.commit()

    return user_note



if __name__ == '__main__':
    from server import app
    connect_to_db(app)

