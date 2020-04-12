from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.etudiant import EtudiantModel

class Etudiant(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('classe',
                        type=str,
                        required=True,
                        help="This field has to be filled"
                        )
    parser.add_argument('ecole_id',
                        type=int,
                        required=True,
                        help="Référence à la classe nécessaire"
                        )

    @jwt_required()
    def get(self, name):
        etudiant = EtudiantModel.find_by_name(name)
        if etudiant:
            return etudiant.json()
        return {"message": "Etudiant non trouvé"},404

    @jwt_required()
    def post(self, name):

        if EtudiantModel.find_by_name(name):
            return {"message":f"Un étudiant avec le même nom existe {name}"},400

        data = Etudiant.parser.parse_args()
        etudiant = EtudiantModel(name, **data)

        try:
            etudiant.save_to_db()
        except:
            return {"message":"Une erreur est apparue à l'insertion"}, 500

        return etudiant.json(), 201

    @jwt_required()
    def delete(self, name):
        etudiant = EtudiantModel.find_by_name(name)
        if etudiant:
            etudiant.delete_from_db()
        return {"message": "Etudiant supprimé"}

    @jwt_required()
    def put(self, name):

        data = Etudiant.parser.parse_args()
        etudiant = EtudiantModel.find_by_name(name)

        if etudiant is None:
            etudiant = EtudiantModel(name, **data)
        else:
            etudiant.classe = data["classe"]
            etudiant.ecole_id = data["ecole_id"]
        etudiant.save_to_db()

        return etudiant.json()

class ListeEtudiant(Resource):
    def get(self):
        return {"etudiants" : [x.json() for x in EtudiantModel.find_all()]}