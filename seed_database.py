""" Script to seed database. """

import os
import json 
from random import choice

import crud 
import model 
import server 

# to re-create databse, run dropdb and createdb
os.system("dropdb parks_db")
os.system("createdb parks_db")

#connect to the database and call db.create_all()
model.connect_to_db(server.app)
model.db.create_all()  

#load park data from JSON file and save as variable
with open("data/parks.json") as p:
    park_data = json.loads(p.read())

#create sample of parks to store in a list
parks_in_db = []
for park in park_data:
    external_id, park_code, park_name = (
        park["id"],
        park["parkCode"],
        park["fullName"]
    )

    db_park = crud.create_park(external_id, park_code, park_name)
    parks_in_db.append(db_park)

#add and commit all parks to database
model.db.session.add_all(parks_in_db)
model.db.session.commit()


#create a list of example notes to use randomly when creating sample user notes
notes = [
        "Has dog-friendly trails!",
        "Has Wheelchair accessible trails!",
        "Has waterfalls!",
        "Everyone in our family wants to visit this place!",
        "Great scenic views for photos!",
        "Highly recommended by co-workers!",
        "No reservations required!"
    ]

#create sample of 10 users
for num in range(10):
    username = f"user{num}",
    email = f"user{num}@test.com",
    password = 'test'

    user = crud.create_user(username, email, password)
    model.db.session.add(user)
    
    #create sample of 10 top parks
    for _ in range(10):
        random_park = choice(parks_in_db)
        top_park = crud.create_user_top_park(user.user_id, random_park.park_id)

        model.db.session.add(top_park)

        #create sample of 10 user notes        
        random_note = choice(notes)
        user_note = crud.create_user_note(user.user_id, random_park.park_id, random_note)

        model.db.session.add(user_note)

#commit users, top parks, and all notes to session
model.db.session.commit()

