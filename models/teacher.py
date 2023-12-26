from config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Teacher(db.Model):
    __tablename__ = 'Profesores'

    ProfesorID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Usuarios.UserID'))
    
    # Establece la relación con el modelo Usuarios
   # usuario = db.relationship('Usuarios', back_populates='profesor')
    #AlumnosSinAsignaciones
