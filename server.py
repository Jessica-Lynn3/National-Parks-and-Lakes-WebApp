from flask import Flask, render_template, redirect, flash, session

from model import connect_to_db, db   
import crud      
import parks                     

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
def create_user_account():
    """ Creates user account. """

    return render_template("create-account.html")


@app.route("/login")
def user_login():
    """ User log in. """

    return render_template("login.html")


@app.route("/product-details-page")
def display_product_details():
    """ Displays page with product details (info about this app). """

    return render_template("product-details-page.html")


@app.route("/logged-out")
def user_log_out():
    """ User logs out of session and is told they are succesfully logged out. """

    return render_template("logged-out.html")


@app.route("/place-page/<parkCode>")
def show_place_page(parkCode):
    """ Shows the info for an individual park using its parkCode. """

    park = parks.get_park_details_by_park_code(parkCode)
    print(park)

    return render_template("place-page.html",
                            display_park=park)


@app.route("/search-results")
def show_search_results():
    """ Shows the search results from Search Filter Feature. """

    return render_template("search-results.html")


@app.route("/user-dashboard")
def show_user_dashboard():
    """ Shows the user's dashboard. """

    park_list = parks.get_park_info_for_cards()

    return render_template("user-dashboard.html",
                            park_list=park_list)


@app.route("/user-top-places")
def show_users_top_places():
    """ Show user's Top Places they want to visit. """

    return render_template("user-top-places.html")



if __name__ == '__main__':
    connect_to_db(app)    
    app.run(host='0.0.0.0', debug=True)
