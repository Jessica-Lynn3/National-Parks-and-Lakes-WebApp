import os
import requests
import json

NPS_KEY = os.environ['NPS']
HEADERS = {"Authorization":f'{NPS_KEY}'}

#-------------------------------------------------------------------------------------------
#       GLOBAL API CALL TO PARKS ENDPOINT 
#           -- GIVES BACK BASIC INFO ABOUT EACH PARK TO USE IN SEVERAL FUNCTIONS
#-------------------------------------------------------------------------------------------

parks = 'https://developer.nps.gov/api/v1/parks'
all_parks_payload = {'start': 0, 'limit': 1000, 'api_key': NPS_KEY}
all_parks_res = requests.get(parks, params=all_parks_payload, headers=HEADERS)
# print(type(all_parks_res))  #<class 'requests.models.Response'>

data = all_parks_res.json()
# print(type(data))   #data is a dictionary
parks = data['data']
#print(type(parks)) #parks is a list of dictionaries

#print(parks[0].keys(), "LINE 22") 
    #dict_keys(['id', 'url', 'fullName', 'parkCode', 'description', 
    # 'latitude', 'longitude', 'latLong', 'activities', 'topics', 
    # 'states', 'contacts', 'entranceFees', 'entrancePasses', 'fees', 
    # 'directionsInfo', 'directionsUrl', 'operatingHours', 'addresses', 
    # 'images', 'weatherInfo', 'name', 'designation'])
#print(type(parks[1])) #dictionary

    #--------------------------------------------------------------------
    #       GET PARKS WITH NATURE-TYPE DESIGNATIONS
    #--------------------------------------------------------------------

park_designations = ['National Park', 'National Parks', 'National Scenic Trail', 
                        'National Lakeshore', 'National Seashore', 
                        'National Park & Preserve','National Preserve', 
                        'Wild River', 'National River', 'National Recreation Area', 
                        'National and State Park', 'Parkway']

park_data = []  #park_data will be a list of dictionaries -- each dictionary is a park

for park in parks:   #a park is one dictionary
    designation = park['designation']
    if designation in park_designations:
        park_data.append(park)

#---------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#       GLOBAL API CALL TO THINGS TO DO ENDPOINT 
#           -- GIVES BACK BASIC INFO ABOUT EACH TRAIL
#-------------------------------------------------------------------------------------------

thingstodo_endpoint = 'https://developer.nps.gov/api/v1/thingstodo'
trails_payload = { 'q':'trail', 'start': 0, 'limit': 2000, 'api_key': NPS_KEY}
trails_res = requests.get(thingstodo_endpoint, params=trails_payload, headers=HEADERS)

all_trails = trails_res.json()

trails = all_trails['data'] #a list of dictionaries

trail_data = []  #trail_data will be a list of dictionaries 
                 #   --> each dictionary is info about 1 trail

for trail in trails:
    #print(type(trail)) #dictionary
    relatedParks = trail.get('relatedParks') #a list of dictionaries
    for dictionary in relatedParks:
        park_designation = dictionary.get('designation')
        if park_designation in park_designations:
            trail_data.append(trail)

#print(trail_data[0].keys())
    #dict_keys(['id', 'url', 'title', 'shortDescription', 'images', 'relatedParks', 
    # 'relatedOrganizations', 'tags', 'latitude', 'longitude', 'geometryPoiId', 
    # 'amenities', 'location', 'seasonDescription', 'accessibilityInformation', 
    # 'isReservationRequired', 'ageDescription', 'petsDescription', 'timeOfDayDescription', 
    # 'feeDescription', 'age', 'arePetsPermittedWithRestrictions', 'activities', 
    # 'activityDescription', 'locationDescription', 'doFeesApply', 'longDescription', 
    # 'reservationDescription', 'season', 'topics', 'durationDescription', 
    # 'arePetsPermitted', 'timeOfDay', 'duration', 'credit'])
#print(len(trail_data)) #1004

#-------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------
#                       FUNCTIONS TO USE IN SERVER.PY 
#-------------------------------------------------------------------------------------------

def get_park_info_for_cards():
    """ Returns park data- a list of dictionaries 
    (each dictionary is a park with its info) """
   
    return park_data



def get_park_details_by_park_code(parkCode):
    """ Returns dataset about a park using its park code """

    park_dataset = {}

    for park in park_data:
        if park['parkCode'] == parkCode:
            park_dataset = {'fullName': park['fullName'],
                            'parkId': park['id'],
                            'parkCode': park['parkCode'],
                            'images': park['images'],
                            'url': park['url'],
                            'states': park['states'],
                            'description': park['description'],
                            'latitude': park['latitude'],
                            'longitude': park['longitude'],
                            'directionsInfo': park['directionsInfo'],
                            'directionsUrl': park['directionsUrl'],
                            'weatherInfo': park['weatherInfo']
                            }

    return park_dataset


#print(get_park_details_by_park_code(parkCode='yose'))



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

#print(find_parks_by_state('MI'))



def get_trail_details_by_park_code(parkCode):
    """ Returns dataset about all trails at one park """

    trail_dataset = {}

    for trail in trail_data:
        relatedParks = trail.get('relatedParks') #list of dictionaries
        
        trail_name = trail.get('title')
        trail_url = trail.get('url')
        shortDescription = trail.get('shortDescription')
        season = trail.get('season')
        seasonDescription = trail.get('seasonDescription')
        isReservationRequired = trail.get('isReservationRequired')
        reservationDescription = trail.get('reservationDescription')
        arePetsPermitted = trail.get('arePetsPermitted')
        petsDescription = trail.get('petsDescription')
        arePetsPermittedWithRestrictions = trail.get('arePetsPermittedWithRestrictions')
        trail_amenities = trail.get('amenities')
        accessibilityInformation = trail.get('accessibilityInformation')
        duration = trail.get('duration')
        durationDescription = trail.get('durationDescription')
        timeOfDay = trail.get('timeOfDay')
    
        for dictionary in relatedParks:
            park_code = dictionary.get('parkCode')

            if park_code == parkCode:
                    trail_dataset= { 'trail_name': trail_name,
                                    'trail_url': trail_url,
                                    'shortDescription': shortDescription, 
                                    'season': season, 
                                    'seasonDescription': seasonDescription,
                                    'isReservationRequired': isReservationRequired, 
                                    'reservationDescription': reservationDescription,
                                    'arePetsPermitted': arePetsPermitted, 
                                    'petsDescription': petsDescription,
                                    'arePetsPermittedWithRestrictions': arePetsPermittedWithRestrictions,
                                    'arePetsPermittedWithRestrictions': trail_amenities, 
                                    'accessibilityInformation': accessibilityInformation,
                                    'duration': duration, 
                                    'durationDescription': durationDescription, 
                                    'timeOfDay': timeOfDay}

    return trail_dataset

print(get_trail_details_by_park_code(parkCode='yell'))

