from flask import Blueprint

conatcts = Blueprint('contacts', __name__)


@conatcts.route('/')
def home():
    return "Contacts List"


@conatcts.route('/new')
def add_contact():
    return "saving a contact"