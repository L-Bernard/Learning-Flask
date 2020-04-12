from db import db

class EcoleModel(db.Model):
    __tablename__ = 'ecole'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80))

    etudiants = db.relationship("EtudiantModel", lazy="dynamic")

    def __init__(self, nom):
        self.nom = nom

    def json(self):
        return {'id' : self.id, 'nom' : self.nom, "etudiants": [etudiant.json() for etudiant in self.etudiants.all()]}

    @classmethod
    def find_by_name(cls, nom):
        return cls.query.filter_by(nom=nom).first()

    @classmethod
    def find_all(cls, nom):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()