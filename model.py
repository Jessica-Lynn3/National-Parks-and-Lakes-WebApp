""" Models for National Parks and Lakes App """

#importing SQLAlchemy
from doctest import debug_script
from flask_sqlalchemy import SQLAlchemy

#calling SQLAlchemy constructor function to create a SQLAlchemy instance at the variable db
db = SQLAlchemy()

#name of database: destinations_db

#Create User Class
class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id}, Username username={self.username}, email={self.email}, password={self.password}>"


#Create Place Class

#Create User Top Place Class

#Create User Note Class


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

    connect_to_db(app)  

