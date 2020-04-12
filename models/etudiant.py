from db import db

class EtudiantModel(db.Model):
    __tablename__ = 'etudiant'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80))
    classe = db.Column(db.String(80))
    ecole_id = db.Column(db.Integer, db.ForeignKey("ecole.id"))
    ecole = db.relationship("EcoleModel")
    #db.Float(precision=2)

    def __init__(self, nom, classe, ecole_id):
        self.nom = nom
        self.classe = classe
        self.ecole_id = ecole_id

    def json(self):
        return {'nom' : self.nom, "classe": self.classe}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(nom=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()