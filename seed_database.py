""" Script to seed database. """

import os
import json 
from random import choice, randint 

import crud 
import model 
import server 

os.system("dropdb parks_db")
os.system("createdb parks_db")

model.connect_to_db(server.app)
model.db.create_all()  

with open("data/parks.json") as p:
    park_data = json.loads(p.read())

parks_in_db = []
for park in park_data:
    external_id, park_code, park_name = (
        park["id"],
        park["parkCode"],
        park["fullName"]
    )

    db_park = crud.create_park(external_id, park_code, park_name)
    parks_in_db.append(db_park)

model.db.session.add_all(parks_in_db)
model.db.session.commit()

