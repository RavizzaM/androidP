from config import db
from datetime import datetime

class Mesas(db.Model):
    __tablename__ = 'Mesas'

    MesaID = db.Column(db.Integer, primary_key=True)
    MateriaID = db.Column(db.Integer, nullable=False)
    ProfesorID = db.Column(db.Integer, nullable=False)
    Fecha = db.Column(db.DateTime, nullable=False)
    