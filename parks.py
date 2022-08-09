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
# print(type(data))   #dictionary

find_total = data['total']
# print(find_total)   #468 parks total

# get_keys = data.keys()
# print(get_keys) 
    #dict_keys(['total', 'limit', 'start', 'data'])

park_data = data['data']
# print(type(park_data)) #list 
# print(park_data)


def get_park_info_for_cards():
    """ Makes request to NPS API and returns each park's 
    parkCode, fullName, and image url """

    park_data = data['data']
   
    return park_data

#get_park_info_for_cards()


def get_park_details_by_park_code(parkCode):
    """ """

    park_data = data['data']

    park_dataset = {}

    for i in park_data:
        #for each dict in park_data
        #get key
        #set as parkcode as key - value is a dictionary with info I want
   
        park_dataset[i['parkCode']] = {'fullName': i['fullName'],
                                        'url': i['url'],
                                        'states': i['states'],
                                        'description': i['description'],
                                        'latLong': i['latLong']}


    #print(park_dataset)

    return park_dataset


#get_park_details_by_park_code(parkCode='yose')