""" Models for National Parks and Lakes App """

#importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#calling SQLAlchemy constructor function to create a SQLAlchemy instance at the variable db
db = SQLAlchemy()

#name of PostgreSQL database: parks_db

#Create User Class
class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    top_parks = db.relationship('UserTopPark', back_populates="users") #Connects to "users" in UserTopPark Class
    notes = db.relationship('UserNote', back_populates="users") #Connects to "users" in UserNote Class
    
 
    def __repr__(self):
        return f"<User -- user_id={self.user_id}, username={self.username}, email={self.email}>"


#Create Park Class
class Park(db.Model):
    """ A National Park """

    __tablename__ = "parks"

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    external_id = db.Column(db.Text)
    park_code = db.Column(db.String, nullable=False)
    park_name = db.Column(db.Text, nullable=False)  
 

    top_parks = db.relationship('UserTopPark', back_populates="parks") #Connects to "parks" in UserTopPark Class
    notes = db.relationship('UserNote', back_populates="parks") #Connects to "parks" in UserNote Class

    def __repr__(self):
        return f"<Park -- park_id={self.park_id}, park_code={self.park_code}, park_name={self.park_name}>"


#Create User Top Park Class
class UserTopPark(db.Model):
    """ A User-Rated Top Park """

    __tablename__ = "user_top_parks"

    user_top_park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))

    users = db.relationship('User', back_populates="top_parks") #Connects to "top_places" in User Class
    parks = db.relationship('Park', back_populates="top_parks") #Connects to "top_places" in Place Class

    def __repr__(self):
        return f"<User Top Park -- user_top_park_id={self.user_top_park_id}, user_id={self.user_id}, park_id={self.park_id}>"


#Create User Note Class
class UserNote(db.Model):
    """ A User Note for a Park """

    __tablename__ = "user_notes"

    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))
    note = db.Column(db.Text)

 
    users = db.relationship('User', back_populates="notes") #Connects to "notes" in User Class
    parks = db.relationship('Park', back_populates="notes") #Connects to "notes" in Park Class

    def __repr__(self):
        return f"<User Note -- note_id={self.note_id}, user_id={self.user_id}, park_id={self.park_id}, note={self.note}>"



def connect_to_db(flask_app, db_uri="postgresql:///parks_db", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri #the location of database
    flask_app.config["SQLALCHEMY_ECHO"] = False  #set to False for now; can change back to echo later
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

    db.app = flask_app 
    db.init_app(flask_app) 

    print("Connected to the db!") 

if __name__ == "__main__":
    from server import app

    #If program outout gets to be too much, call connect_to_db(app, echo=False)
    #This will tell SQLAlchemy not to print out every query it executes

    connect_to_db(app, echo=False)   

