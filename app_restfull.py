from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from ressources.user import UserRegister
from ressources.etudiant import Etudiant, ListeEtudiant
from ressources.ecole import Ecole, ListeEcole
from db import db
from os import getenv

#from secret_settings import *

from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.secret_key = "A super secret API key"
app.secret_key = getenv("SECRET_KEY")
api = Api(app)

app.config['JWT_AUTH_USERNAME_KEY'] = 'nom_authent'
app.config['JWT_AUTH_URL_RULE'] = '/authent'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity)

api.add_resource(Etudiant, "/etudiant/<string:name>")
api.add_resource(ListeEtudiant, "/etudiant")
api.add_resource(Ecole, "/ecole/<string:name>")
api.add_resource(ListeEcole, "/ecole")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)