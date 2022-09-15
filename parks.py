import os, json
import requests
# import json
from bs4 import BeautifulSoup 
# import states_and_park_codes 

NPS_KEY = os.environ['NPS']
HEADERS = {'Authorization':f'{NPS_KEY}', 'Content-Type': 'application/json'}

#-------------------------------------------------------------------------------------------
#        API CALL TO PARKS ENDPOINT 
#           -- GIVES BACK BASIC INFO ABOUT EACH PARK TO USE IN SEVERAL FUNCTIONS
#-------------------------------------------------------------------------------------------

PARK_DESIGNATIONS = ['National Park', 'National Parks', 'National Scenic Trail', 
                     'National Lakeshore', 'National Seashore', 
                     'National Park & Preserve','National Preserve', 
                     'Wild River', 'National River', 'National Recreation Area', 
                     'National and State Park', 'Parkway']

def request_parks(): 
    url = 'https://developer.nps.gov/api/v1/parks'
    payload = {'start': 0, 'limit': 1000, 'api_key': NPS_KEY}
    all_parks_res = requests.get(url, params=payload, headers=HEADERS)
    # print(type(all_parks_res))  #<class 'requests.models.Response'>

    data = all_parks_res.json()
    # print(type(data))   #data is a dictionary
    return data['data']
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


def get_park_designations():
    park_data = []  #park_data will be a list of dictionaries -- each dictionary is a park
    parks = request_parks()
    
    for park in parks:   #a park is one dictionary
        designation = park['designation']
        if designation in PARK_DESIGNATIONS:
            park_data.append(park)
    return park_data
    
# print(park_data, "PARK DATA!!!")

#---------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#        API CALL TO THINGS TO DO ENDPOINT 
#           -- GIVES BACK BASIC INFO ABOUT EACH TRAIL
#-------------------------------------------------------------------------------------------


def request_park_activities(state):
    url = 'https://developer.nps.gov/api/v1/thingstodo'
    payload = {'q': 'trail', 'stateCode': state,'start': 0, 'limit': 2000, 'api_key': NPS_KEY}
    response = requests.get(url, params=payload, headers=HEADERS)
    trails = response.json()
    return trails['data'] #a list of dictionaries

    #print(trails, 'TRAILS!!!')


def get_park_designation_activities(state=None):
    trail_data = []  #trail_data will be a list of dictionaries 
                     #   --> each dictionary is info about 1 trail
    activities = request_park_activities(state)
    
    for trail in activities: 
        for park in trail.get('relatedParks'):
            if park.get('designation') in PARK_DESIGNATIONS:
                trail_data.append(trail)
    return trail_data

# print(trail_data, "TRAIL DATA!!!")

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
#                       FUNCTIONS TO USE IN SERVER.PY RE: PARK DATA
#-------------------------------------------------------------------------------------------

def get_park_details_by_park_code(parkCode):
    """ Returns dataset about a park using its park code """
    parks = get_park_designations() 
    park_dataset = {}

    for park in parks:
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
                            'weatherInfo': park['weatherInfo']}
    return park_dataset


#print(get_park_details_by_park_code(parkCode='yose'))


def get_trail_details_by_park_code(parkCode, state=None):
    """ Returns dataset about all trails at one park """

    park_trails = request_park_activities(state)

    trails = []
    
    for trail in park_trails:
        relatedParks = trail.get('relatedParks', [])
        if relatedParks:
            for park in relatedParks:
                if parkCode == park.get('parkCode'):
                    trails.append(trail)

    return trails


#-------------------------------------------------------------------------------------------
#              FUNCTIONS TO USE IN SERVER.PY RE: TRAIL DATA 
#-------------------------------------------------------------------------------------------

def get_trails_by_park_code(parkCode):
    """ Returns dataset about all trails at one park """

    activities = get_park_designation_activities()
    trails = []
    
    for trail in activities:
        #print(type(trail)) #dict
        relatedParks = trail.get('relatedParks', [])
        if relatedParks:
            for park in relatedParks:
                if parkCode == park.get('parkCode'):
                    #print(trail) #dict -- info about one trail
                    trail['add key'] = 'KEY ADDED!!!!!'
                    #print(trail) #This works! Key added!
                    trails.append(trail)
                    #print(trail.get('add key')) #prints out value of key
    #print(trails[0].get('add key')) #to get key from list
    return trails

#get_trail_details_by_park_code(parkCode='acad')




#-------------------------------------------------------------------------------------------
#              FUNCTIONS TO USE TO FIND PARKS RE: SEARCH FILTER OPTION
#-------------------------------------------------------------------------------------------

def filter_parks_with_dog_friendly_trails(parks):
    """ Returns dictionary of parks that have pet-friendly trails """
    parks_pet_friendly_trails = []

    for park in parks:
        if park.get('arePetsPermitted') == "true":
           parks_pet_friendly_trails.append(park)
           
    return parks_pet_friendly_trails

#print(find_parks_with_dog_friendly_trails())

def find_parks_with_accessible_trails():
    """ Returns dictionary of parks that have wheelchair accessible trails """

    
    parks_accessible_trails = {}
        
    # parkCodes_w_a11y_trails = ['acad', 'appa', 'arch', 'asis', 'badl', 'bawa', 'bibe', 
    #                             'bicy', 'bith', 'blri', 'brca', 'buff', 'cana', 'cany', 
    #                             'caco', 'care', 'cuva', 'deva', 'dewa', 'ever', 'fiis',
    #                             'jeff', 'gate', 'glca'] #will add more
                                 

    # for park in park_data:
    #     if park['parkCode'] in parkCodes_w_a11y_trails:
    #         parks_accessible_trails[park['fullName']] = {'parkCode': park['parkCode'],
    #                                                         'images': park['images'],
    #                                                         'states': park['states']}
        
    return parks_accessible_trails

#print(find_parks_with_accessible_trails())



def find_parks_by_state(state, parks):
    """ Returns parks and their info by one state location --
    For example: state = 'CA' --> returns all CA parks and their info """


    #---------------------------------------------------
    #     1) Find parks using state argument passed in 
    #---------------------------------------------------
    parks_by_state = []

    for park in parks:
        if state in park['states']:
            parks_by_state.append(park)
    
    return parks_by_state 


#find_parks_by_state('DE')
# find_parks_by_state('NH')
# find_parks_by_state('CA')





#-------------------------------------------------------------------------------------------
#       FUNCTIONS THAT TRIED TO USE BEAUTIFUL SOUP TO REMOVE HTML TAGS FROM TRAIL INFO
#-------------------------------------------------------------------------------------------
    # On webpage, html tags were being passed through from the API and were
    # being displayed on the page

    # Tried to use Beautiful Soup
    #   - The remove_html_tags() function works without accessing API, 
    #      instead passing in html string as argument in the function call: 
    #                   - Result: in terminal all html tags were removed
    #   - However, did not work with API call:
    #                   - Result: the html tags were still there
    #
    # Bottom line: BeautifulSoup works but not with API call

def remove_html_tags(html):
    """ Removes html tags passed in from API """

    # soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())
    # print(soup.get_text())

    #----------------------------------------------
    #     Code below tries applying API call
    #----------------------------------------------
    # Note: deleted html param to run function -- not using any param 
    #   - instead will pass api value I want into BeautifullSoup constructor
    #
    # for trail in trail_data:
    #     a11y_info = trail['accessibilityInformation']
    # #     print(a11y_info)
    # #     print(type(a11y_info))
    #     soup = BeautifulSoup(a11y_info, "html.parser") #doesn't work
        #print(soup.get_text()) #doesn't work

    soup = BeautifulSoup(html, "html.parser")

    return soup.get_text()

# print(remove_html_tags('<style>Testing</style>Works? <br>BREAK<br /> Test 2<p>'))
# print(remove_html_tags('<p><meta charset="utf-8" />Dogs must be on a leash no longer than 6 feet.</p>'))
#remove_html_tags()




