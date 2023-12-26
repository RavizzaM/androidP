from config import db
from datetime import datetime

class Examen_Calendario(db.Model):
    __tablename__ = 'MesasEx'
    __table_args__ = {'info': dict(is_view=True)}


    MesaID = db.Column(db.Integer, primary_key = True)
    Fecha = db.Column(db.Date)
    NombreMateria = db.Column(db.String)
    Descripcion = db.Column(db.String)
    Profesor = db.Column(db.String)
    

    def to_dict(self):
        # Formatear la fecha en el formato deseado
        formatted_date = self.Fecha.strftime("%Y-%m-%d")

        user_dict = {
            'MesaID': self.MesaID,
            'Fecha': formatted_date,  # Usar la fecha formateada
            'NombreMateria': self.NombreMateria,
            'Descripcion': self.Descripcion,
            'Profesor': self.Profesor
        }
        return user_dict