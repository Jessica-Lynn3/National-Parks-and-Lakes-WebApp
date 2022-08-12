import os
import requests
import json

NPS_KEY = os.environ['NPS']
HEADERS = {"Authorization":f'{NPS_KEY}'}

parks = 'https://developer.nps.gov/api/v1/parks'

all_parks_payload = {'start': 0, 'limit': 1000, 'api_key': NPS_KEY}

all_parks_res = requests.get(parks, params=all_parks_payload, headers=HEADERS)
# print(type(all_parks_res))
    #<class 'requests.models.Response'>

data = all_parks_res.json()
# print(type(data))   #data is a dictionary

parks = data['data']
print(type(parks)) #parks is a list of dictionaries

park_designations = ['National Park', 'National Parks', 'National Scenic Trail', 
                        'National Lakeshore', 'National Seashore', 
                        'National Park & Preserve','National Preserve', 
                        'Wild River', 'National River', 'National Recreation Area', 
                        'National and State Park']

park_data = []  #park_data is a list of dictionaries

for park in parks:   #a park is one dictionary
    designation = park['designation']
    if designation in park_designations:
        park_data.append(park)

#print(type(park_data))


def get_park_info_for_cards():
    """ Returns park data- a list of dictionaries 
    (each dictionary is a park with its info) """
   
    return park_data



def get_park_details_by_park_code(parkCode):
    """ Returns dataset about a park using its park code """

    park_dataset = {}

    for park in park_data:
        #for each park in park_data
        #get key
        #set parkcode as key - value is a dictionary with info I want
   
        park_dataset[park['parkCode']] = {'fullName': park['fullName'],
                                        'url': park['url'],
                                        'states': park['states'],
                                        'description': park['description'],
                                        'latLong': park['latLong']}



    return park_dataset


#get_park_details_by_park_code(parkCode='yose')



def find_parks_by_state(state):
    """ Returns parks and their info by one state location --
    For example: state = 'CA' --> returns all CA parks and their info """

    parks_by_state = {}

    for park in park_data:
        if state in park['states']:
            parks_by_state[park['fullName']] = {'parkCode': park['parkCode'],
                                                'states': park['states'],
                                                'images': park['images']}

    return parks_by_state

# find_parks_by_state('MI')




