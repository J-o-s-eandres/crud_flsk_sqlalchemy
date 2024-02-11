from flask import Flask
from routes.contacts import contacts
from utils.db import db


app = Flask(__name__)

app.secret_key='secret key'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/contactsDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa la instancia de SQLAlchemy con tu aplicación Flask

app.register_blueprint(contacts)


