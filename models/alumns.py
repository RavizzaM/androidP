from config import db


class AlumnosSinAsignaciones(db.Model):
    __tablename__ = 'AlumnosSinAsignaciones'
    __table_args__ = {'info': dict(is_view=True)}

    UserID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(80), nullable=False)
    Apellido = db.Column(db.String(120), nullable=False)
    CorreoElectronico = db.Column(db.String(120), nullable=False)
    Tipo = db.Column(db.String(120), nullable=False)
    Contrasena = db.Column(db.String(120), nullable=False)
    AlumnoID = db.Column(db.Integer, primary_key=False)

    def to_dict(self):
        user_dict = {
            'UserID': self.UserID,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'CorreoElectronico': self.CorreoElectronico,
            'Tipo': self.Tipo,
            'Contrasena': self.Contrasena,
            'AlumnoID': self.AlumnoID
        }
        return user_dict

