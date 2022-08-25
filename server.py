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
        flash(f"Welcome back, {user.username}".title())
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
    print(park_info, "PARK DATASET")

    # Instead of using lines 139 - 143 below --> use lines 146 - 149:  
    # return render_template("place-page.html",
    #                        park_info=park_info,
    #                        park_code=park_info.get("parkCode"),
    #                        park_id=park_info.get("parkId"),
    #                        park_name=park_info.get("fullName"))
    
    #Getting all the same info -- instead using json here -- this is cleaner:
    return render_template("place-page.html",
                           park_info=park_info,
                           json_park_info=json.dumps(park_info))



@app.route("/bookmark-park", methods=["POST"])
def bookmark_park():
    park_info = json.loads(request.form.get('park-info'))
    print(park_info)
    if park_info:
        park = crud.get_park(park_info['parkId'])
        print(park)
        if not park:
            park = crud.create_park(park_info['parkId'], park_info['parkCode'], park_info['fullName'])
    
    if 'user_id' in session and session['user_id']:
        user_id = session['user_id']

        # implement a check if UserTopPark already contains an object with the user_id and the park.park_id
        # if it does exist, then don't create a new one
        # if it does not exist, create a new one

        exists = crud.get_user_top_park(user_id, park.park_id)
        print(exists, "LINE 170")
        print(type(exists))

        
        if exists == None: 
            user_park = crud.create_user_top_park(user_id, park.park_id)
            print(f'Top Park {user_park.user_top_park_id} created!')
            flash(f'Top Park {user_park.user_top_park_id} created!')
    
        # return redirect(f'/place-page/{park_info["parkCode"]}')
    return redirect('/user-dashboard')
        



@app.route("/search-results")
def show_search_results():
    """ Shows the search results from Search Filter Feature. """

    state = request.args.get("state")

     # make sure input from form is turned into a string
    state = str(state).upper()

    parks_by_state = parks.find_parks_by_state(state)
    print(parks_by_state)
    
    return render_template("search-results.html", parks_by_state=parks_by_state)



@app.route("/user-top-places")
def show_users_top_places():
    """ Show user's Top Places they want to visit. """

    return render_template("user-top-places.html")



@app.route("/user-top-places", methods=["POST"])
def save_top_park():
    """ User can write note about why they want to visit park.
    Park and Note are saved to User info in database """

    #also need to display park 'card' like on user dashboard
    #   will want to pass in park_data (route /user-dashboard )

    return render_template("user-top-places.html")


if __name__ == '__main__':
    connect_to_db(app)    
    app.run(debug=True)
