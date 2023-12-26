from config import db

class MateriasLista(db.Model):
    __tablename__ = 'Materias_con_profesores'
    __table_args__ = {'info': dict(is_view=True)}


    ProfesorID = db.Column(db.Integer, primary_key = True)
    NombreMateria = db.Column(db.String)
    MateriaID = db.Column(db.Integer, primary_key = True)
    Apellido = db.Column(db.String)
    Nombre = db.Column(db.String)
    CorreoElectronico = db.Column(db.String)

    def to_dict(self):
        user_dict = {
            'ProfesorID': self.ProfesorID,
            'NombreMateria': self.NombreMateria,
            'MateriaID': self.MateriaID,
            'Apellido': self.Apellido,
            'Nombre': self.Nombre,
            'CorreoElectronico': self.CorreoElectronico
        }
        return user_dict

