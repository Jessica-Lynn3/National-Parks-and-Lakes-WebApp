from flask import Flask, render_template, redirect, request, flash, session, jsonify

from model import connect_to_db, db   
import crud      
import parks                     
import json
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = 'SECRET_SECRET_SECRET'  

app.jinja_env.undefined = StrictUndefined


#Routes and View Functions below

@app.route("/")
def display_homepage():
    """ View homepage. """

    return render_template("homepage.html")



@app.route("/create-account")
def display_create_account_page():
    """ View Create Account Page. """

    return render_template("create-account.html")



@app.route("/create-account", methods=["POST"])
def create_user_account():
    """ Creates user account. """

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("Cannot create an account with that email.  Try again.")
    else:
        user = crud.create_user(username=username, email=email, password=password)
        flash("Account created!  Please log in.")

    return render_template("login.html")



@app.route("/login", methods=["GET"])
def display_login_page():
    """ User log in. """

    return render_template("login.html")



@app.route("/login", methods=["POST"])
def user_login():
    """ User log in. """

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The username, email or password you entered were incorrect.  Try again")
        return redirect("/login")
    else:
        session["username"] = user.username
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.username}!".title())
        return redirect("/user-dashboard")



@app.route("/product-details-page")
def display_product_details():
    """ Displays page with product details (info about this app). """

    return render_template("product-details-page.html")



@app.route("/logged-out")
def user_log_out():
    """ User logs out of session and is told they are succesfully logged out. """

    
    return render_template("logged-out.html")



@app.route("/user-dashboard")
def go_back_to_user_dashboard():
    """ Shows the user's dashboard. """


    park_data = parks.get_park_info_for_cards()

    return render_template("user-dashboard.html",
                            park_data=park_data)



@app.route("/user-dashboard", methods=["POST"])
def show_user_dashboard():
    """ Shows the user's dashboard. """

    park_data = parks.get_park_info_for_cards()

    return render_template("user-dashboard.html",
                            park_data=park_data)



@app.route("/search-filter-page")
def submit_search_filter():
    """ Submits user input (state code) and returns parks within that state 
    on the search results page """

    return render_template("search-filter-page.html")


@app.route("/place-page/<parkCode>")
def show_place_page(parkCode):
    """ Shows the info for an individual park using its parkCode. """

    park_info = parks.get_park_details_by_park_code(parkCode)
    
    trail_info = parks.get_trail_details_by_park_code(parkCode)
    # print([trail.get('relatedParks') for trail in trail_info], 'RELATED PARKS!!!!')
    
    return render_template("place-page.html",
                           park_info=park_info,
                           json_park_info=json.dumps(park_info),
                           trail_info=trail_info)



@app.route("/bookmark-park", methods=["POST"])
def bookmark_park():
    """ User bookmarks a park.  Creates a Top Park that is saved to user account. """
    
    #grab park-info from form
    park_info = json.loads(request.form.get('park-info'))
    print(park_info)

    #if park_info use crud.py to get park.park_id
    if park_info:
        park = crud.get_park(park_info['parkId'])
        print(park)
        #if park doesn't exist yet, create park
        if not park:
            park = crud.create_park(park_info['parkId'], park_info['parkCode'], park_info['fullName'])
    
    #if user in session get their user_id
    if session['user_id']:
        user_id = session['user_id']

        # implement a check if UserTopPark already contains an object with the user_id and the park.park_id
        # if it does exist, then don't create a new one
        # if it does not exist, create a new one

        exists = crud.get_user_top_park(user_id, park.park_id)
        print(exists, "LINE 177")
        print(type(exists))

        
        if exists == None: 
            user_park = crud.create_user_top_park(user_id, park.park_id)
            print(f'Top Park {user_park.user_top_park_id} created!')
            flash(f'Top Park {user_park.user_top_park_id} created!')
        
        else:
            flash('This park has already been added to your Top Parks!')
    
    return redirect(f'/place-page/{park_info["parkCode"]}')
    
        


@app.route("/save-note/<parkCode>", methods=["POST"])
def save_note(parkCode):
    """ Returns note about a park as JSON.  Saves note to database """
    # FIRST need to implement check here:
    #   - for user to save note, park has to be a Top Park
    #   - if it's a Top Park -- park has been created and saved to db

     #Grab note from form
    # note_contents = request.form.get('park-note')

    #get value from AJAX
    note_contents = request.json.get('note')

    #print(parkCode)

    #if user in session get their user_id
    if session['user_id']:
        user_id = session['user_id']
        park = crud.get_park_by_parkCode(parkCode)
        print(park)

    #Grab park from User's Top Parks in db
    top_park_exists = crud.get_user_top_park(user_id, park.park_id)

    if top_park_exists == None:
        flash('To write a note for this park, first save it as a Top Park')

    if top_park_exists:
        new_note = crud.create_user_note(user_id, park.park_id, note_contents)
        print(f'Note {new_note.note_id} created!')
        flash(f'Note {new_note.note_id} created!')

    #crud.py call to applicable park_id, to get note about that park
    note_from_db = crud.get_user_note(user_id, park.park_id, note_contents)
    
    return jsonify(note_from_db.note)
   


@app.route("/search-results", methods=["GET", "POST"])
def show_search_results():
    """ Shows the search results from Search Filter Feature. """

    state = request.args.get("state")

     # make sure input from form is turned into a string
    state = str(state).upper()
    parks_by_state = parks.find_parks_by_state(state)
    #print(parks_by_state)

    # find_pet_trails = parks.find_parks_with_dog_friendly_trails() #returns dictionary
    # find_wh_access_trails = parks.find_parks_with_accessible_trails()

    # value_set = [find_pet_trails, find_wh_access_trails]

    if request.method == 'POST':
        value_set = request.form.getlist('search-filter')
        if value_set == ['pet-trails']:
            #return html page and pass in dictionary from parks.py
            return render_template('search-results.html', parks_by_state=parks_by_state)
        elif value_set == ['a11y-trails']:
            return render_template('search-results.html', parks_by_state=parks_by_state)
        elif value_set == ['pet-trails', 'a11y-trails']:
            return 'Display BOTH pet trails and accessible trails'


    return render_template("search-results.html")
                                                # find_pet_trails=find_pet_trails,
                                                # find_wh_access_trails=find_wh_access_trails)



@app.route("/user-top-places")
def show_users_top_places():
    """ Show user's Top Places they want to visit. """

    park_data = parks.get_park_info_for_cards()
    # print(type(park_data)) #a list of dictionaries
    # print("LINE 254")
    # print(park_data[0]) # 1 dictionary

    #get user-id
    if session['user_id']:
        user_id = session['user_id']   
   
    #get all of user's Top Parks
    all_top_parks = crud.get_all_user_top_parks(user_id)
    print(all_top_parks) #a list of UserTopPark objects

    top_parkCodes = []

    #loop through list and get park_code
    for item in all_top_parks:
        park_code = item.parks.park_code
        #print(park_code)
        top_parkCodes.append(park_code)
    #print(top_parkCodes, "LINE 270")

    top_parkCodes_no_dupes = set(top_parkCodes)

    top_park_data = []

    #loop through top_parkCodes_no_dupes and park_data
    #   if park-Code matches park_data's park['parkCode']
    #   append park (a dictionary) to top_park_data
    for park_code in sorted(top_parkCodes_no_dupes):
      for park in park_data:
          if park_code == park['parkCode']:
              top_park_data.append(park)

    #print(top_park_data)
    print(top_parkCodes_no_dupes)
    

    return render_template("user-top-places.html",
                            top_park_data=top_park_data)



if __name__ == '__main__':
    connect_to_db(app)    
    app.run(debug=True)
