from flask import Flask, jsonify, render_template, redirect, flash, session

# from model import connect_to_db, db   #database in progress - will add this once db created
# import crud                           #will import crud once db created

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secret'  #will modify this later

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


@app.route("/place-page") #this will be implemented more later (want to pass in place_id in url)
def show_place_page():
    """ Shows the page for an individual place (a park or a lake). """

    return render_template("place-page.html")


@app.route("/search-results")
def show_search_results():
    """ Shows the search results from Search Filter Feature. """

    return render_template("search-results.html")


@app.route("/user-dashboard")
def show_user_dashboard():
    """ Shows the user's dashboard. """

    return render_template("user-dashboard.html")


@app.route("/user-top-places")
def show_users_top_places():
    """ Show user's Top Places they want to visit. """

    return render_template("user-top-places.html")



if __name__ == '__main__':
    # connect_to_db(app)    #will add this once database created
    app.run(host='0.0.0.0', debug=True)
