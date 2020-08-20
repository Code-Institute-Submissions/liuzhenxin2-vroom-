from flask import Flask, flash, render_template, request, redirect, url_for
import os
import pymongo
from dotenv import load_dotenv
from bson.objectid import ObjectId
import datetime

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "vroom"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]

# Main page route


@app.route("/")
def show_index():
    return render_template("index.html")

@app.route("/all_listings")
def show_all_listings():
    listings = db.listings.find()
    return render_template("all_listings.template.html", listings=listings)

# Create a listing page
@app.route("/create")
def show_create():
    car_brand = db.brands.find()
    return render_template("create_listing.template.html", car_brand=car_brand)


@app.route("/create", methods=["POST"])
def process_create():

    # retrieve information from the create form
    brand_id = request.form.get("car_brand")
    car_model = request.form.get("car_model")
    car_type = request.form.get("car_type")
    car_hp = request.form.get("car_hp")
    car_condition = request.form.get("car_condition")
    car_year = request.form.get("car_year")
    car_price = request.form.get("car_price")
    car_mileage = request.form.get("car_mileage")

    # check for error messages

    #accumulator

    errors = {}

    # check if name of car brand has at least 2 letters

    if len(car_model) < 2:
        errors.update(
            model_too_short="Please key in at least 2 letters for car model.")

    if len(errors) > 0:
        car_brand = db.brands.find()
        flash("Unable to create listing", "danger")
        # previous_values = request.form.to_dict()
        # previous_values['car_brand'] = ObjectId(previous_values['car_brand'])
        previous_values = request.form
        return render_template("create_listing.template.html", errors=errors, previous_values=previous_values, car_brand=car_brand)

    # fetch the info of the brand by its ID

    car_brand = db.brands.find_one({
        '_id': ObjectId(brand_id)
    })

    # fetch the info of the user by its ID

    # create the query

    new_listing = {
        #'_id' : ObjectId(user_id),
        #'seller_name' : user_info["name"],
        #'seller_contact' : user_info["contact"]["phone"],
        'car': {
            '_id': ObjectId(brand_id),
            'car_brand': car_brand["brand"],
            'car_model': car_model,
            'car_type': car_type,
            'car_hp': car_hp,
            'car_condition': car_condition,
            'car_year': car_year,
            'car_price': car_price,
            'car_mileage': car_mileage
        }
    }

    # execute the query

    db.listings.insert_one(new_listing)

    flash("New listing has been created!", "success")

    return redirect(url_for('show_created'))

# Show Created listing


@app.route("/created/<listing_id>")
def show_created(listing_id):
    new_listing = db.listings.find({}).sort("_id", -1).limit(1)
    car_brand = db.brands.find()
    return render_template("created_listing.template.html", new_listing=new_listing)

@app.route("/updated/<listing_id>")
def show_updated(listing_id):
    car_brand =db.brands.find()
    listing = db.listings.find_one({
        '_id': ObjectId(listing_id)
    })
    return render_template("updated_listing.template.html", listing=listing)

@app.route("/update/<listing_id>")
def show_update(listing_id):
    listing = db.listings.find_one({
        '_id': ObjectId(listing_id)
    })
    car_brand = db.brands.find()

    return render_template("update_listing.template.html", listing=listing, car_brand=car_brand)

@app.route("/update/<listing_id>", methods=["POST"])
def process_update(listing_id):
    brand_id = request.form.get("car_brand")
    car_model = request.form.get("car_model")
    car_type = request.form.get("car_type")
    car_hp = request.form.get("car_hp")
    car_condition = request.form.get("car_condition")
    car_year = request.form.get("car_year")
    car_price = request.form.get("car_price")
    car_mileage = request.form.get("car_mileage")

    car_brand = db.brands.find_one({
        '_id': ObjectId(brand_id)
    })

    listing = db.listings.find_one({
        '_id': ObjectId(listing_id)
    })

    db.listings.update_one({
        '_id': ObjectId(listing_id)
    },
        {
        '$set': {
            'car': {
                '_id': ObjectId(brand_id),
                'car_brand': car_brand["brand"],
                'car_model': car_model,
                'car_type': car_type,
                'car_hp': car_hp,
                'car_condition': car_condition,
                'car_year': car_year,
                'car_price': car_price,
                'car_mileage': car_mileage
            }
        }
    })
    return redirect(url_for('show_updated', listing_id=listing_id))

@app.route("/delete/<listing_id>")
def show_delete_listing(listing_id):
    listing = db.listings.find_one({
        '_id' : ObjectId(listing_id)
    })
    return render_template("delete_listing.template.html", listing=listing)

@app.route("/delete/<listing_id>", methods=["POST"])
def process_delete_listing(listing_id):
    db.listings.remove({
        '_id' : ObjectId(listing_id)
    })
    return redirect(url_for("show_all_listings"))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
