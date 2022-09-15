#   dictionary format:
#       trails_by_parkCode = 'parkCode': [ { "title": "",
#                                            "accessibilityInformation": "",  
#                                            "isWheelchairAccessible": ""     #ADD THIS AS True/False value    
#                                         } ]

    # To add more to dictionary-- copy code below and fill in blanks:
      # 'parkCode': 
      #     [ {
      #         "title": "",
      #         "accessibilityInformation": "",     
      #         "isWheelchairAccessible": "" 
      #       } 
      #     ],


def get_all_trail_a11y_by_parkCode():
    """ Returns dictionary with all trail info
    -- parkcodes are the keys """

    trails_a11y = {
                        'appa':   #appa has 4 trails total
                            [{
                                "title": "Multi-Park Loop",
                                "accessibilityInformation": "The Normanstone Trail, Whitehaven Trail, and Glover-Archbold Park Trail can be muddy, rugged, and narrow. These trails are not recommended for those who experience difficulty moving over rough terrain. Anyone wanting to attempt this hike can alter it to suit their needs by proceeding through Georgetown and remaining on sidewalks to get to Dumbarton Oaks Park and Montrose Park. Proceeding along city streets will provide visitors with the opportunity to view the architecture of Georgetown homes. The C&O Canal, Mount Vernon Trail and the National Mall are accessible.",
                                "isWheelchairAccessible": "False"
                        },
                        {
                                "title": "Visit The Point at Harpers Ferry",
                                "accessibilityInformation": "The Point is accessible to all visitors though the current gravel path may pose some problems to those with physical limitations. The Lower Town area of Harpers Ferry does have some uneven and textured surfaces. All visitors should watch their footing while exploring the town.",
                                "isWheelchairAccessible": "False"
                        },
                        {
                                "title": "Visit John Brown's Fort",
                                "accessibilityInformation": "John Brown's Fort is accessible to all visitors. The Lower Town area of Harpers Ferry does have some uneven and textured surfaces. All visitors should watch their footing while exploring the town.",
                                "isWheelchairAccessible": "True"
                        },
                        {
                                "title": "Visit Jefferson Rock",
                                "accessibilityInformation": "Due to the nature of the trail - steep stairs, uneven surfaces - Jefferson Rock is not accessible to those with physical limitations.There are other vistas of the water gap in Lower Town, such as The Point, that are accessible to all. Please inquire at the Information Center or Visitor Center regarding all of the park's vistas.",
                                "isWheelchairAccessible": "False"
                        }],

                        'acad': #there are 52 trails total for acad
                            [ {
                                "title": "Hike Gorham Mountain Loop",
                                "accessibilityInformation": "The Gorham Mountain Loop is not accessible. The trail has uneaven footing and a few places where scrambling over rocks is required. Be aware the Cadillac Cliff trail addition on this hike does involve rungs and ladders.",     
                                "isWheelchairAccessible": "False" 
                              },
                            {
                                "title": "Stargazing on Cadillac Mountain (Vehicle Access Limited)",
                                "accessibilityInformation": "The parking lots and portions of Cadillac Summit Loop are accessible. Extra caution is required after dark. There is an accessible restroom at the summit.",
                                "isWheelchairAccessible": "True"
                              },
                            {
                                "title": "Go Earthcaching At Acadia",
                                "accessibilityInformation": "This activity requires hiking on trails and uneven surfaces. It is not wheelchair accessible. Screen readers can be utilized to read the clues. ",     
                                "isWheelchairAccessible": "False"
                              },
                              {
                                "title": "Drive Cadillac Mountain",
                                "accessibilityInformation": "Parking: At the two summit parking lots, a limited number of designated accessible parking spaces are marked. These are reserved for vehicles displaying an accessibility placard or license plate. Pullout parking is unmarked and may be sloped. Trails: Portions of the Cadillac Summit Loop are paved, wide enough for a single wheelchair, and provide scenic views of Frenchman Bay and the Porcupine Islands. Other sections are very steep or contain steps up and down. All other trails to and around Cadillac Mountain are not accessible. Facilities and Services Cadillac Mountain Gift Shop has an accessible entrance and restrooms.",     
                                "isWheelchairAccessible": "True"
                              }, 
                              {
                                "title": "Hike Great Head Trail",
                                "accessibilityInformation": "The Great Head Trail is not wheelchair accessible. The trail has uneven footing and a few places where scrambling over rocks is required. There is accessible parking at the Sand Beach parking areas as well as accessible restrooms.",     
                                "isWheelchairAccessible": "False"
                              },
                              {
                                "title": "Hike Ship Harbor Trail",
                                "accessibilityInformation": "The first loop is ADA compliant. Second loop is mostly flat with occasional log framed steps and plank trail. Restrooms (vault toilets) at trailhead are not accessible. Park in the Ship Harbor parking lot west of Seawall Campground on Route 102 A. The first one-quarter mile (0.4 km) is a hard-packed surface leading to the mudflats. Access to intertidal pools is over rocky, uneven terrain. Steep grades will require assistance. Total distance is 1.3 miles (2.1 km) round trip.",     
                                "isWheelchairAccessible": "True"
                              } 
                            ],
                            

    }

    for parkCode, trail_data in trails_a11y.items():
        print(type(parkCode)) #parkCode is key - a string
        print(type(trail_data)) #trail_data is value - a list of dictionaries
        for item in trail_data:
                # print(type(item)) #dict
                # print(item.keys())
                print(item.get('isWheelchairAccessible'))
                print(item.get('accessibilityInformation'))


    return trails_a11y

get_all_trail_a11y_by_parkCode()