import sqlite3

from flask_restful import Resource, reqparse
from models.usermodel import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nom_authent',
                        type=str,
                        required=True,
                        help="This field has to be filled"
    )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field has to be filled"
     )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["nom_authent"]):
            return {"message":"User déjà existant"},400

        user = UserModel(**data) #**data= data["nom_authent"], data["password"]
        user.save_to_db()

        return {"message":"Utilisateur créé"}, 201
