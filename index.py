from app import app
from utils.db import db


# Crea las tablas definidas en el modelo
with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)