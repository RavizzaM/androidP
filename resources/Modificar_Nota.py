from flask_restful import Resource, reqparse
from config import db
from models.Examenes import Examenes
from datetime import datetime

class Modificar_Nota(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('AlumnoID', type=int, required=True)
            parser.add_argument('MateriaID', type=int, required=True)
            parser.add_argument('ProfesorID', type=int, required=True)
            parser.add_argument('Fecha', type=str, required=True)
            parser.add_argument('NuevaCalificacion', type=int, required=True)
            args = parser.parse_args()

            # Convertir la cadena de fecha en un objeto 'datetime'
            fecha_str = args['Fecha']
            fecha_datetime = datetime.strptime(fecha_str, "%Y-%m-%d")  # Ajustar el formato de la fecha según sea necesario

            # Verificar si existe el registro de examen con los filtros proporcionados
            examen = Examenes.query.filter_by(
                AlumnoID=args['AlumnoID'],
                MateriaID=args['MateriaID'],
                ProfesorID=args['ProfesorID'],
                Fecha=fecha_datetime
            ).first()

            if examen:
                # Actualizar la calificación
                examen.Calificacion = args['NuevaCalificacion']
                db.session.commit()
                return {'message': 'Calificación actualizada correctamente'}, 200
            else:
                return {'error': 'No se encontró el registro para actualizar'}, 404

        except Exception as e:
            # Manejar cualquier excepción ocurrida durante la actualización
            return {'error': str(e)}, 500
