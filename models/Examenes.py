from config import db
from datetime import datetime

class Examenes(db.Model):
    __tablename__ = 'Examen'
    __table_args__ = {'extend_existing': True}

    NotaID = db.Column(db.Integer, primary_key=True)
    AlumnoID = db.Column(db.Integer, nullable=False)
    MateriaID = db.Column(db.Integer, nullable=False)
    ProfesorID = db.Column(db.Integer, nullable=False)
    Fecha = db.Column(db.DateTime, nullable=False)
    Calificacion = db.Column(db.Integer, nullable=False)