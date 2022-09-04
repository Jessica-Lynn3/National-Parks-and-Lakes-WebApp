import os, json
import requests
# import json
from bs4 import BeautifulSoup 
import trail_info_no_html_tags 

NPS_KEY = os.environ['NPS']
HEADERS = {'Authorization':f'{NPS_KEY}', 'Content-Type': 'application/json'}

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
    
# print(park_data, "PARK DATA!!!")

#---------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#       GLOBAL API CALL TO THINGS TO DO ENDPOINT 
#           -- GIVES BACK BASIC INFO ABOUT EACH TRAIL
#-------------------------------------------------------------------------------------------

thingstodo_endpoint = 'https://developer.nps.gov/api/v1/thingstodo'
trails_payload = { 'q':'trail', 'start': 0, 'limit': 2000, 'api_key': NPS_KEY}
trails_res = requests.get(thingstodo_endpoint, params=trails_payload, headers=HEADERS)

all_trails = trails_res.json()

trails_data_no_html_tags = all_trails['data'] #a list of dictionaries

#print(trails, 'TRAILS!!!')

trail_data = []  #trail_data will be a list of dictionaries 
                 #   --> each dictionary is info about 1 trail

for trail in trails_data_no_html_tags:
    #print(type(trail)) #dictionary
    relatedParks = trail.get('relatedParks') #a list of dictionaries
    for dictionary in relatedParks:
        park_designation = dictionary.get('designation')
        if park_designation in park_designations:
            trail_data.append(trail)

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



#-------------------------------------------------------------------------------------------
#              FUNCTIONS TO USE IN SERVER.PY RE: TRAIL DATA 
#-------------------------------------------------------------------------------------------

def get_trail_details_by_park_code(parkCode):
    """ Returns dataset about all trails at one park """

    trails = []
    
    for trail in trail_data:
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

def find_parks_with_dog_friendly_trails():
    """ Returns dictionary of parks that have pet-friendly trails """

    parks_pet_friendly_trails = {}
    
    parkCodes_w_pet_trails = ['acad', 'amis', 'appa', 'asis', 'badl', 'bibe', 'bith',
                                'bisc', #'blca', 
                                'blri', 'boha', 'brca', 'buff', 'cana', 'cany', 'caco',
                                'care', 'cave', 'chis', 'chat', #'cong', 'cure'
                                'cuva', 'deva', 'dena', 'ever', 'fiis', 'jeff', 'gate',
                                'glca', 'goga', 'grca', 'grba', 'grsa', 'grsm', 'gumo',
                                'guis', 'hale', 'hosp', 'indu', 'jotr', 'kefj', 'lacl',
                                'laro', 'lavo', 'maca', 'meve', 'moja', 'mora', 'natt', 
                                'natr', 'noca', 'pefo', 'piro', 'pore', 'pohe', 'romo',
                                'samo', 'seki', 'shen', 'slbe', 'tapr', 'thro', 'vall', 
                                'voya', 'whis', 'wica', 'wrst', 'yell', 'yose', 'zion']

    for park in park_data:
        if park['parkCode'] in parkCodes_w_pet_trails:
            parks_pet_friendly_trails[park['fullName']] = {'parkCode': park['parkCode'],
                                                            'images': park['images'],
                                                            'states': park['states']}

    
    return parks_pet_friendly_trails

#print(find_parks_with_dog_friendly_trails())



def find_parks_with_accessible_trails():
    """ Returns dictionary of parks that have wheelchair accessible trails """

    
    parks_accessible_trails = {}
        
    parkCodes_w_a11y_trails = ['acad', 'appa', 'arch', 'asis', 'badl', 'bawa', 'bibe', 
                                'bicy', 'bith', #'blca', 
                                'blri', 'brca', 'buff', 'cana', 'cany', 'caco', 'care',
                                'cuva'] #'cong', 'cure'
                                 

    for park in park_data:
        if park['parkCode'] in parkCodes_w_a11y_trails:
            parks_accessible_trails[park['fullName']] = {'parkCode': park['parkCode'],
                                                            'images': park['images'],
                                                            'states': park['states']}
        
    return parks_accessible_trails



def find_parks_by_state(state):
    """ Returns parks and their info by one state location --
    For example: state = 'CA' --> returns all CA parks and their info """

    states_with_parks_from_API = [ "AL","AK","AZ","AR","CA","CO","CT",
                                  "DC","FL","GA","HI","ID","IN","KS",
                                  "KY","ME","MD","MA","MI","MN","MS",
                                  "MO","MT","NV","NH","NJ","NM","NY",
                                  "NC","ND","OH","OK","OR","PA","SC",
                                  "SD","TN","TX","UT","VT","VA","WA",
                                  "WV","WI","WY"]

    states_with_no_parks_from_API = ["DE","IL","IA","LA","NE","RI","VI"]

    no_parks_message = "No parks were found. This state does not have any parks which the National Park Service qualify as one of these park designations: National Park, National Parks, National and State Park, National Park & Preserve, National Preserve, National Scenic Trail, National Lakeshore, National Seashore,  Wild River, National River, Parkway. Try searching for parks in another state. "

    parks_by_state = {}

    for park in park_data:
        if state in park['states']:
            parks_by_state[park['fullName']] = {'parkCode': park['parkCode'],
                                                'states': park['states'],
                                                'images': park['images']}
  
    by_state = parks_by_state

    a11y = find_parks_with_accessible_trails()
    pets = find_parks_with_dog_friendly_trails()

    #add both dicts to one dict

    one_dict = {} 
    
    one_dict['accessible'] = a11y
    one_dict['pets'] = pets
    one_dict['by_state'] = by_state

    print(one_dict.get('by_state'))

    print(one_dict.keys())

    return one_dict

#find_parks_by_state('DE')
find_parks_by_state('NH')
# find_parks_by_state('VT')



def get_info():

    a11y = find_parks_with_accessible_trails()
    pets = find_parks_with_dog_friendly_trails()

    #add both dicts to one dict

    one_dict = {} 
    
    one_dict['accessible'] = a11y
    one_dict['pets'] = pets

    #print(one_dict.get('pets'))
    return one_dict

#get_info()


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




