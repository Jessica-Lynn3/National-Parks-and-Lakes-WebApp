

def get_parkCodes_by_state():
    """ Returns dictionary with parkCodes relevant to state
    -- state codes are the keys """

    states_and_parkCodes = {
                            "AL": ['liri','natt','natr'],
                            "AK": ['alag','bela','dena','gaar','glba','katm',
                                    'kefj','kova','lacl','noat','wrst','yuch'],
                            "AZ": ['glca','grca','lake','pefo','sagu'],
                            "AR": ['buff','hosp'], 
                            "CA": ['chis','deva','goga','jotr','lavo','moja',
                                    'pinn','pore','samo','seki','whis','yose'],
                            "CO": ['blca','cure','grsa','meve','romo'],
                            "CT": ['appa','neen'],
                            
                            "DE": [""" 
                                    No parks were found.  

                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],
                            
                            "DC": ['pohe'],
                            "FL": ['bicy','bisc','cana','drto','ever','guis'],
                            "GA": ['appa','chat','cuis'],
                            "HI": ['hale','havo'],
                            "ID": ['yell'],
                            
                            "IL": [ """ 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],
                            
                            "IN": ['indu'],
                            
                            "IA": [ """ 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],

                            "KS": ['tapr'],
                            "KY": ['maca'],

                            "LA": [ """ 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],

                            "ME": ['acad','appa'],
                            "MD": ['appa','asis','bawa','pohe'],
                        #check page! did I accidentally delete a code?

                            "MA": ['appa','boha','caco','neen'],
                            "MI": ['isro','noco','piro','slbe'],
                            "MN": ['noco','voya'],
                            "MS": ['guis','natt','natr'],
                            "MO": ['jeff'],
                            "MT": ['bica','glac','yell'],

                            "NE": [ """ 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],

                            "NV": ['deva','grba','lake'],
                            "NH": ['appa'],
                            "NJ": ['appa','dewa','gate'],
                            "NM": ['cave','vall','whsa'],
                            "NY": ['appa','flis','gate','noco'],
                            "NC": ['appa','blri','caha','calo','grsm'],
                            "ND": ['noco','thro'],
                            "OH": ['cuva','noco'],
                            "OK": ['chic'],
                            "OR": ['crla'],
                            "PA": ['appa','dewa','noco','pohe'],

                            "RI": [ """ 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """],

                            "SC": ['cong'],
                            "SD": ['badl','wica'],
                            "TN": ['appa','grsm','natt','natr'],
                            "TX": ['amis','bibe','bith','gumo','lamr','pais'],
                            "UT": ['arch','brca','cany','care','glca','zion'],
                            "VT": ['appa','noco'],
                            "VA": ['appa','asis','blri','pohe','shen'],
                            "WA": ['laro','mora','noca','olym'],
                            "WV": ['appa','gari'],
                            "WI": ['apis','iatr','noco'],
                            "WY": ['bica','grte','yell'],

                            "VI": [""" 
                                    No parks were found.  
                                    
                                    This state does not have any parks which the National Park Service qualify 
                                    as one of these park designations: National Park, National Parks, 
                                    National and State Park, National Park & Preserve, National Preserve, 
                                    National Scenic Trail, National Lakeshore, National Seashore,  Wild River, 
                                    National River, Parkway.
                                    
                                    Try searching for parks in another state. """]
    }

    return states_and_parkCodes 

get_parkCodes_by_state()


