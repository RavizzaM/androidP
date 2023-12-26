from flask import jsonify
from flask_restful import Resource
from models.Profesores_Lista import ProfesoresLista  # Importa el modelo de la vista

class Profesoreslista(Resource):
    def get(self):
        # Realiza la consulta a la vista
        query_result = ProfesoresLista.query.all()

        # Verifica si hay resultados
        if not query_result:
            return {'error': 'No se encontraron datos en la vista'}, 404

        # Convierte los resultados a formato JSON
        Lista_profesores = [
            {
                'Apellido': result.Apellido,
                'Nombre': result.Nombre,
                'CorreoElectronico': result.CorreoElectronico,
                'NombreMateria': result.NombreMateria,
                'ProfesorID': result.ProfesorID
                

            }
            for result in query_result
        ]

        return jsonify({'Lista_profesores': Lista_profesores})