from flask import jsonify
from flask_restful import Resource
from models.alumns import AlumnosSinAsignaciones
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

class AlumnsResource(Resource):
    def get(self, apellido):
        # Normalizar el apellido ingresado
        apellido = remove_accents(apellido).lower()

        # Filtra los alumnos por apellido
        query_result = AlumnosSinAsignaciones.query.filter(AlumnosSinAsignaciones.Apellido.ilike(f'%{apellido}%')).all()

        # Verificar si hay resultados
        if not query_result:
            return {'error': 'No se encontraron alumnos con el apellido proporcionado'}, 404

        # Convertir los resultados a formato JSON
        alumnos_sin_asignaciones = [
            {'UserID': result.UserID, 'Nombre': result.Nombre, 'Apellido': result.Apellido,
             'CorreoElectronico': result.CorreoElectronico, 'Tipo': result.Tipo, 'AlumnoID': result.AlumnoID}
            for result in query_result
        ]

        return jsonify({'alumnos': alumnos_sin_asignaciones})


