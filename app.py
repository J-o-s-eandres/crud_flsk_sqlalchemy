from flask import Flask
from routes.contacts import conatcts

app = Flask(__name__)

app.register_blueprint(conatcts)

