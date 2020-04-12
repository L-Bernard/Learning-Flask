from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ecole import EcoleModel

class Ecole(Resource):

    @jwt_required()
    def get(self, name):
        ecole = EcoleModel.find_by_name(name)
        if ecole:
            return ecole.json()
        return {"message": "Ecole non trouvée"}, 404

    @jwt_required()
    def post(self, name):

        if EcoleModel.find_by_name(name):
            return {"message":f"Une école avec le même nom existe {name}"},400

        ecole = EcoleModel(name)

        try:
            ecole.save_to_db()
        except:
            return {"message":"Une erreur est apparue à l'insertion"}, 500

        return ecole.json(), 201

    @jwt_required()
    def delete(self, name):
        ecole = EcoleModel.find_by_name(name)
        if ecole:
            ecole.delete_from_db()
        return {"message": "Ecole supprimée"}


class ListeEcole(Resource):
    def get(self):
        return {"ecoles" : [ecole.json() for ecole in EcoleModel.find_all()]}