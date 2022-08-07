import os
import requests
import json

NPS_KEY = os.environ['NPS']
HEADERS = {"Authorization":f'{NPS_KEY}'}

parks = 'https://developer.nps.gov/api/v1/parks'

all_parks_payload = {'start': 0, 'limit': 1000, 'api_key': NPS_KEY}

all_parks_res = requests.get(parks, params=all_parks_payload, headers=HEADERS)

data = all_parks_res.json()

find_total = data['total']
# print(find_total)   #468

# get_keys = data.keys()
# print(get_keys) 
    #dict_keys(['total', 'limit', 'start', 'data'])

park_data = data['data']
# print(type(park_data)) #list 


def get_park_info_for_cards():
    """ Makes request to NPS API and returns each park's 
    parkCode, fullName, and image url """

    # for i in park_data:
    #     print(type(i))  #each is a dictionary
    #     get_keys = i.keys()
    #     print(get_keys)

        #dict_keys(['id', 'url', 'fullName', 'parkCode', 'description', 
        #           'latitude', 'longitude', 'latLong', 'activities', 'topics', 
        #           'states', 'contacts', 'entranceFees', 'entrancePasses', 'fees', 
        #           'directionsInfo', 'directionsUrl', 'operatingHours', 'addresses', 
        #           'images', 'weatherInfo', 'name', 'designation'])

    park_list = []

    for i in park_data:
        parkCode = i['parkCode']
        fullName = i['fullName'] 
        images = i['images']    
        for elem in images:
            image_url = elem['url'] 
        basic_info = f'{parkCode}, {fullName}, {image_url}' #this gives me back first url only -- indent to get all urls for that park
        park_list.append(basic_info)

    return park_list

   # print(park_list)

#get_park_info_for_cards()


def get_park_details_by_park_code(parkCode):
    """ """

    park_details = []

    for i in park_data:
        fullName = i['fullName'] 
        park_url = i['url']
        states = i['states']
        description = i['description']
        latLong = i['latLong']
        detail_set = f'{fullName}, {park_url}, {states}, {description}, {latLong}'
        park_details.append(detail_set)

    return park_details

    
#get_park_details_by_park_code()