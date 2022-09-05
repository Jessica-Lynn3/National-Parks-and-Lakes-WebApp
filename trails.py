#   dictionary format:
#       trails_by_parkCode = 'parkCode': [ { "title": "",
#                                              "url": "",
#                                               "shortDescription": "",
#                                               "doFeesApply": "",
#                                               "isReservationRequired": "",
#                                               "arePetsPermitted": "",
#                                               "petsDescription": "",
#                                               "accessibilityInformation": "",     
#                                               "season": "Winter, Spring, Summer, Fall"
#                                         } ]



def get_all_trail_info_by_parkCode():
    """ Returns dictionary with all trail info
    -- parkcodes are the keys """

    trails_by_parkCode = {
                        'appa':   #appa has 4 trails total
                            [{
                                "url": "https://www.nps.gov/thingstodo/10-mile-multi-park-loop.htm",
                                "title": "Multi-Park Loop",
                                "shortDescription": "Park your car and stretch your legs! Visit four different National Parks in Washington, DC and begin logging miles on seven different National Historic or National Scenic trails!",
                                "accessibilityInformation": "The Normanstone Trail, Whitehaven Trail, and Glover-Archbold Park Trail can be muddy, rugged, and narrow. These trails are not recommended for those who experience difficulty moving over rough terrain. Anyone wanting to attempt this hike can alter it to suit their needs by proceeding through Georgetown and remaining on sidewalks to get to Dumbarton Oaks Park and Montrose Park. Proceeding along city streets will provide visitors with the opportunity to view the architecture of Georgetown homes. The C&O Canal, Mount Vernon Trail and the National Mall are accessible.",
                                "isReservationRequired": "false",
                                "petsDescription": "Pets are allowed on trails within Rock Creek Park but must adhere to the B.A.R.K. Ranger Principles. Dogs must always be on a leash within the park. Waste must be carried out and disposed of in trash receptacles. For more information on B.A.R.K. Ranger visit the Pets section of the National Park Service website.",
                                "doFeesApply": "false",
                                "season": "Winter, Spring, Summer, Fall",
                                "arePetsPermitted": "true",
                        },
                        {
                                "url": "https://www.nps.gov/thingstodo/visit-the-point.htm",
                                "title": "Visit The Point at Harpers Ferry",
                                "shortDescription": "Visit where the Potomac and Shenandoah rivers meet! From this location, known as The Point, you look upon three states - Maryland, Virginia, and West Virginia - as well as the confluence of the two rivers. We invite you to visit in any season to gaze upon the magnificent sight of this water gap in the Blue Ridge Mountains.",
                                "accessibilityInformation": "The Point is accessible to all visitors though the current gravel path may pose some problems to those with physical limitations. The Lower Town area of Harpers Ferry does have some uneven and textured surfaces. All visitors should watch their footing while exploring the town.",
                                "isReservationRequired": "false",
                                "petsDescription": "Leashed pets are allowed at The Point. Please visit our Pets page to learn more about visiting Harpers Ferry National Historical Park with your pets.",
                                "doFeesApply": "true",
                                "season": "Winter, Spring, Summer, Fall",
                                "arePetsPermitted": "true",
                        },
                        {
                                "url": "https://www.nps.gov/thingstodo/visit-john-browns-fort.htm",
                                "title": "Visit John Brown's Fort",
                                "shortDescription": "A visit to John Brown's Fort is more than seeing the building where John Brown and several of his followers barricaded themselves in 1859. The building has a complex history that begins in 1848, continues through to today, and includes four locations in Harpers Ferry and one in Chicago. We invite you to visit this famous Harpers Ferry building and discover what it means to you.",
                                "accessibilityInformation": "John Brown's Fort is accessible to all visitors. The Lower Town area of Harpers Ferry does have some uneven and textured surfaces. All visitors should watch their footing while exploring the town.",
                                "isReservationRequired": "false",
                                "petsDescription": "Pets are not allowed inside of the building.",
                                "doFeesApply": "true",
                                "season": "Winter, Spring, Summer, Fall",
                                "arePetsPermitted": "true",
                        },
                        {
                                "url": "https://www.nps.gov/thingstodo/visit-jefferson-rock.htm",
                                "title": "Visit Jefferson Rock",
                                "shortDescription": "Hike along the Appalachian Trail in Harpers Ferry, WV to see the view Thomas Jefferson once described as one of the most stupendous scenes in Nature.",
                                "accessibilityInformation": "Due to the nature of the trail - steep stairs, uneven surfaces - Jefferson Rock is not accessible to those with physical limitations.There are other vistas of the water gap in Lower Town, such as The Point, that are accessible to all. Please inquire at the Information Center or Visitor Center regarding all of the park's vistas.",
                                "isReservationRequired": "false",
                                "petsDescription": "Leashed pets are allowed at Jefferson Rock. Please visit the Pets section of the National Park Service website to learn more about visiting Harpers Ferry National Historical Park with your pets.",
                                "doFeesApply": "true",
                                "season": "Winter, Spring, Summer, Fall",
                                "arePetsPermitted": "true",
                        }],

                        'parkCode': 
                            [ {
                                "title": "",
                                "url": "",
                                "shortDescription": "",
                                "doFeesApply": "",
                                "isReservationRequired": "",
                                "arePetsPermitted": "",
                                "petsDescription": "",
                                "accessibilityInformation": "",     
                                "season": "Winter, Spring, Summer, Fall"
                              } 
                            ],

                        'acad': #there are 52 trails total for acad
                            [ {
                                "title": "Hike Gorham Mountain Loop",
                                "url": "https://www.nps.gov/thingstodo/hike-gorham-mountain-loop.htm",
                                "shortDescription": "The Gorham Mountain Loop is 3.5 miles featuring mountains and a rocky coastline with panoramic views of Mount Desert Island, Frenchman Bay, and the outlying islands.",
                                "doFeesApply": "False",
                                "isReservationRequired": "False",
                                "arePetsPermitted": "True",
                                "petsDescription": "Dogs must be on a leash no longer than 6 feet. Please pack out and place in a waste receptical all dog waste in Acadia National Park.",
                                "accessibilityInformation": "The Gorham Mountain Loop is not accessible. The trail has uneaven footing and a few places where scrambling over rocks is required. Be aware the Cadillac Cliff trail addition on this hike does involve rungs and ladders.",     
                                "season": "Spring, Summer, Fall"
                              },
                            {
                                "title": "Stargazing on Cadillac Mountain (Vehicle Access Limited)",
                                "url": "https://www.nps.gov/thingstodo/stargazing-cadillac.htm",
                                "shortDescription": "Gaze in awe at Acadia's night sky from the highest mountain summit in the park.",
                                "doFeesApply": "False",
                                "isReservationRequired": "False",
                                "arePetsPermitted": "True",
                                "petsDescription": "Pets must be on a leash, no longer than six feet, at all times.",
                                "accessibilityInformation": "The parking lots and portions of Cadillac Summit Loop are accessible. Extra caution is required after dark. There is an accessible restroom at the summit.",     
                                "season": "Spring, Summer, Fall"
                              },
                            {
                                "title": "Go Earthcaching At Acadia",
                                "url": "https://www.nps.gov/thingstodo/acadia-earthcache.htm",
                                "shortDescription": "Embark on an exciting journey through time to discover how glaciers have shaped Acadia National Park. Using your GPS unit and a set of clues obtained from this website and hidden along the journey, you can guide yourself to a series of sites in the park.",
                                "doFeesApply": "True",
                                "isReservationRequired": "True",
                                "arePetsPermitted": "True",
                                "petsDescription": "Leashed pets are allowed on most trails in the park. Please pick up after your pet and dispose of any pet waste in a trash container and be aware of weather and terrain conditions that may affect your pet. ",
                                "accessibilityInformation": "This activity requires hiking on trails and uneven surfaces. It is not wheelchair accessible. Screen readers can be utilized to read the clues. ",     
                                "season": "Spring, Summer, Fall"
                              },
                              {
                                "title": "Drive Cadillac Mountain",
                                "url": "https://www.nps.gov/thingstodo/drive-cadillac-mountain.htm",
                                "shortDescription": "Cadillac Mountain is a popular destination for visitors to Acadia National Park. Accessible by car, it is the highest point on the eastern seaboard of the U.S., and offers magnificent views of a glaciated coastal and island landscape. The short, paved Cadillac Summit Loop Trail, interpretive waysides, restrooms, and gift shop are located at the summit.",
                                "doFeesApply": "True",
                                "isReservationRequired": "True",
                                "arePetsPermitted": "True",
                                "petsDescription": "Pets must be on a leash 6 feet (2 m) or shorter.",
                                "accessibilityInformation": "Parking: At the two summit parking lots, a limited number of designated accessible parking spaces are marked. These are reserved for vehicles displaying an accessibility placard or license plate. Pullout parking is unmarked and may be sloped. Trails: Portions of the Cadillac Summit Loop are paved, wide enough for a single wheelchair, and provide scenic views of Frenchman Bay and the Porcupine Islands. Other sections are very steep or contain steps up and down. All other trails to and around Cadillac Mountain are not accessible. Facilities and Services Cadillac Mountain Gift Shop has an accessible entrance and restrooms.",     
                                "season": "Spring, Summer, Fall"
                              }, 
                              {
                                "title": "Hike Great Head Trail",
                                "url": "https://www.nps.gov/thingstodo/hike-great-head-trail.htm",
                                "shortDescription": "This 1.7 mile trail has spectacular ocean views along a coastal headland with some wooded sections. This historic trail also includes the ruins of an early 1900's tea house.",
                                "doFeesApply": "False",
                                "isReservationRequired": "False",
                                "arePetsPermitted": "True",
                                "petsDescription": "Dogs must be on a leash no longer than 6 feet. Between May 15 and September 15, dogs are only permitted on Sand Beach long enough to cross to the trail head.",
                                "accessibilityInformation": "The Great Head Trail is not wheelchair accessible. The trail has uneven footing and a few places where scrambling over rocks is required. There is accessible parking at the Sand Beach parking areas as well as accessible restrooms.",     
                                "season": "Winter, Spring, Summer, Fall"
                              },
                              {
                                "title": "Hike Ship Harbor Trail",
                                "url": "https://www.nps.gov/thingstodo/hike-ship-harbor-trail.htm",
                                "shortDescription": "Ship Harbor Trail is a 1.3 mile figure-8 loop near Seawall. Great for families and birders, and a variety of habitats can be seen along the shore.",
                                "doFeesApply": "False",
                                "isReservationRequired": "False",
                                "arePetsPermitted": "True",
                                "petsDescription": "Go to link for this park's information regarding pets",
                                "accessibilityInformation": "The first loop is ADA compliant. Second loop is mostly flat with occasional log framed steps and plank trail. Restrooms (vault toilets) at trailhead are not accessible. Park in the Ship Harbor parking lot west of Seawall Campground on Route 102 A. The first one-quarter mile (0.4 km) is a hard-packed surface leading to the mudflats. Access to intertidal pools is over rocky, uneven terrain. Steep grades will require assistance. Total distance is 1.3 miles (2.1 km) round trip.",     
                                "season": "Spring, Summer, Fall"
                              } 
                            ],
                            

    }

    for trail, trail_data in trails_by_parkCode.items():
        print(type(trail))
        print(type(trail_data))
        for item in trail_data:
                # print(type(item)) #dict
                # print(item.keys())
                print(item.get('season'))


    return trails_by_parkCode 

get_all_trail_info_by_parkCode()