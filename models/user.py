from config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'Usuarios'

    UserID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(80), nullable=False)
    Apellido = db.Column(db.String(120), nullable=False)
    CorreoElectronico = db.Column(db.String(120), nullable=False)
    Tipo = db.Column(db.String(120), nullable=False)
    Contrasena = db.Column(db.VARBINARY(256), nullable=False)
    Salt = db.Column(db.VARBINARY(32), nullable=False)
    HashedPassword = db.Column(db.VARBINARY(64), nullable=False)


    #profesor = db.relationship('Profesores', uselist=False, back_populates='usuario')
    
    def to_json(self):
        user_dict = {
            'UserID': self.UserID,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'CorreoElectronico': self.CorreoElectronico,
            'Tipo': self.Tipo
        }
        return user_dict
