
![Banner-Blue-Mountains](/static/images/Banner-Mountains.png)
### Wilderness Awaits: A National Parks and Lakes Web App 

- Wilderness Awaits is a full-stack web application that allows users to find National Park trails and activities to help users decide their next National Park adventure. 

![Homepage-Carousel-Image-2](/static/images/Homepage-2.png)
##### Higlighted Features:
- Users can customize their search and find trails and activities that are pet-friendly, trails and activities that do not require reservations, and find out the accessibility information for the respective trails and activities from the National Park Service API.

![Homepage-Carousel-Image-3](/static/images/Homepage-3.png)
##### Purpose:
- This app was built to provide National Park enthusiasts with a means to customize their next adventure based upon their needs, and to provide up-to-date park information via the National Park Service API.

--------------

## Table of Contents

### [Technologies Used](#technologies-used)
### [Exploring the App](#exploring-the-app)
- [User Registration and Login](#user-registration-and-login)
- [User Dashboard](#user-dashboard)
- [Park Page](#park-page)
- [Saving A Park](#saving-a-park)
- [Search Filter](#search-filter)

----------------

### Technologies Used:
- Python, PostgreSQL, SQLAlchemy, Flask, Jinja2, HTML, Bootstrap, CSS, JavaScript, JSON, AJAX
- So that users will always have access to the most up to date information about National Parks, all park data displayed within this app is performed via calls to the National Park Service API.

![Tech Stack](/static/images/Tech-Stack.png)

--------------

### Exploring the App

![Homepage-Carousel-Image-1](/static/images/Homepage-with-Account-Login.png)

#### User Registration and Login
##### Users are able to register for an account and login; this data is stored using a Postgres relational database.  

![Login](/static/images/Login.png)


#### User Dashboard
##### After making a call to the API, I used Jinja templating to loop over the park data sets and render them in HTML as Bootstrap cards on the user dashboard.

![User Dashboard 1](/static/images/User-Dashboard-1.png)

##### Users can scroll through Park cards . . . 
![User Dashboard 1](/static/images/User-Dashboard-2.png)

##### . . . and can click on each park to explore further details provided on the park’s page.

#### Park Page

![Park Page](/static/images/Park-Page.png)

###### For each park page, basic park details are displayed . . .

![Basic Park Info](/static/images/Basic-Info.png)

##### . . . as well as park trails and activities displayed via a Bootstrap accordion.  Here users can find more specific information regarding activities.

![Park Activities Info](/static/images/Park-Activities-Info.png)

#### Saving A Park
##### When users save the park to their account— a request is made to my Flask server to persist the user’s saved park in the database.  Once a Top Park, users can write a note to remind them why they want to visit that park.  Notes are displayed via an AJAX request, and then stored with the user’s info in the database.

![Save Park and Write Note](/static/images/Save-Park-and-Write-Note.png)

#### Search Filter
##### With the search filter, users can also search for trails and activities within a state, to find trails and activities that are pet-friendly and do not require reservations.

![Search Filter](/static/images/Search-Filter.png)
![Search Results 1](/static/images/Search-Results-1.png)
![Search Results 2](/static/images/Search-Results-2.png)

##### Users can easily refer back to parks they want to visit on their Top Parks Page.

![Top Parks Page](/static/images/Top-Parks-Page.png)

----------------

#### Future Plans
##### 2.0 plans are in progress.  These will be implemented prior to deployment and include: 
- providing more options by working with the National Park Service API and the DOM, 
- and installing the Google Maps API and it’s Places Library for users to further customize their next adventure.

-----------------

#### About
##### Jessica is a software engineering student in the San Francisco Bay Area.  She looks forward to beginning her journey in tech and building apps that would benefit the lives of others.

