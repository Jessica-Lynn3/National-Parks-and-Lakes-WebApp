""" Models for National Parks and Lakes App """

#importing datetime and SQLAlchemy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

#calling SQLAlchemy constructor function to create a SQLAlchemy instance at the variable db
db = SQLAlchemy()

#name of PostgreSQL database: destinations_db

#Create User Class
class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    top_places = db.relationship('User_Top_Place', back_populates="users") #Connects to "users" in User_Top_Place Class
    notes = db.relationship('User_Note', back_populates="user") #Connects to "user" in User_Note Class
    
 
    def __repr__(self):
        return f"<User -- user_id={self.user_id}, username={self.username}, email={self.email}, password={self.password}>"


#Create Place Class
class Place(db.Model):
    """ A place - can be a National Park or a Lake.
    
    Note:   A lake is a place that is not listed as an official National Park.
            A lake is an item in a collection of the Top Ten Largest Lakes in the US.  """

    __tablename__ = "places"

    place_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    external_id = db.Column(db.Integer)
    is_park = db.Column(db.Boolean, nullable=False)
    is_lake = db.Column(db.Boolean, nullable=False)

    place_name = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    state_location = db.Column(db.String)

    website = db.Column(db.Text)
    phone_contact = db.Column(db.BigInteger)
    opens_at = db.Column(db.DateTime)
    closes_at = db.Column(db.DateTime)

    fee_info = db.Column(db.Text)
    reservation_required = db.Column(db.Boolean)
    overview = db.Column(db.Text)
    highlighted_features = db.Column(db.Text)

    trails_easy = db.Column(db.Boolean)
    trails_medium = db.Column(db.Boolean)
    trails_hard = db.Column(db.Boolean)
    trails_dog_friendly = db.Column(db.Boolean)
    trails_accessible = db.Column(db.Boolean)

    beaches_dog_friendly = db.Column(db.Boolean)
    beaches_accessible = db.Column(db.Boolean)
    swimming_allowed = db.Column(db.Boolean)
    boating_allowed = db.Column(db.Boolean)
    beach_open_to_public = db.Column(db.Boolean)

    camping_allowed = db.Column(db.Boolean)
    camper_rv_allowed = db.Column(db.Boolean)

    landscape_photography_allowed = db.Column(db.Boolean)
    season_to_visit = db.Column(db.String)

    top_places = db.relationship('User_Top_Place', back_populates="places") #Connects to "places" in User_Top_Place Class
    note = db.relationship('User_Note', back_populates="place") #Connects to "place" in User_Note Class

    def __repr__(self):
        return f"<Place -- place_id={self.place_id}, place_name={self.place_name}, is_park={self.is_park}, is_lake={self.is_lake}>"


#Create User Top Place Class
class User_Top_Place(db.Model):
    """ A User-Rated Top Place """

    __tablename__ = "user_top_places"

    user_top_place_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))

    users = db.relationship('User', back_populates="top_places") #Connects to "top_places" in User Class
    places = db.relationship('Place', back_populates="top_places") #Connects to "top_places" in Place Class

    def __repr__(self):
        return f"<User Top Place -- user_top_place_id={self.user_top_place_id}>"


#Create User Note Class
class User_Note(db.Model):
    """ A User Note for a Place """

    __tablename__ = "user_notes"

    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))
    note = db.Column(db.Text)

 
    user = db.relationship('User', back_populates="notes") #Connects to "notes" in User Class
    place = db.relationship('Place', back_populates="note") #Connects to "note" in Place Class

    def __repr__(self):
        return f"<User Note -- note_id={self.note_id}, note={self.note}>"



def connect_to_db(flask_app, db_uri="postgresql:///destinations_db", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri 
    flask_app.config["SQLALCHEMY_ECHO"] = echo 
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

    db.app = flask_app 
    db.init_app(flask_app) 

    print("Connected to the db!") 

if __name__ == "__main__":
    from server import app

    #If program outout gets to be too much, call connect_to_db(app, echo=False)
    #This will tell SQLAlchemy not to print out every query it executes

    connect_to_db(app, echo=False)  

