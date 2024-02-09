from flask import Blueprint, render_template

conatcts = Blueprint('contacts', __name__)

@conatcts.route('/')
def home():
    return render_template("index.html")

@conatcts.route('/new')
def add_contact():
    return "saving a contact"

@conatcts.route('/update')
def update_contact():
    return "update a contact"

@conatcts.route('/delete')
def delete_contact():
    return "delete a contact"

@conatcts.route('/about')
def about():
    return render_template("about.html")