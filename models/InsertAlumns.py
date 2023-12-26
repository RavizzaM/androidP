from config import db

class Asignaciones(db.Model):
    __tablename__ = 'Asignaciones'

    AsignacionID = db.Column(db.Integer, primary_key=True)
    ProfesorID = db.Column(db.Integer, nullable=False)
    AlumnoID = db.Column(db.Integer, nullable=False)
    MateriaID = db.Column(db.Integer, nullable=False)