from config import db

class ProfesoresLista(db.Model):
    __tablename__ = 'ListaProfesores'
    __table_args__ = {'info': dict(is_view=True)}


    Apellido = db.Column(db.String)
    Nombre = db.Column(db.String)
    CorreoElectronico = db.Column(db.String)
    NombreMateria = db.Column(db.String)
    ProfesorID = db.Column(db.Integer, primary_key = True)
   
 

    def to_dict(self):
        user_dict = {
            'Apellido': self.Apellido,
            'Nombre': self.Nombre,
            'CorreoElectronico': self.CorreoElectronico,
            'NombreMateria': self.NombreMateria,
            'ProfesorID': self.ProfesorID
            
        }
        return user_dict
