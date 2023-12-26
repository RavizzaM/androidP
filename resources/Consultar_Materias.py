from flask import jsonify
from flask_restful import Resource
from models.Materias_Lista import MateriasLista  # Importa el modelo de la vista

class MateriasListas(Resource):
    def get(self):
        # Realiza la consulta a la vista
        query_result = MateriasLista.query.all()

        # Verifica si hay resultados
        if not query_result:
            return {'error': 'No se encontraron datos en la vista'}, 404

        # Convierte los resultados a formato JSON
        materias_con_profesores = [
            {
                'ProfesorID': result.ProfesorID,
                'NombreMateria': result.NombreMateria,
                'MateriaID': result.MateriaID,
                'Apellido': result.Apellido,
                'Nombre': result.Nombre,
                'CorreoElectronico': result.CorreoElectronico

            }
            for result in query_result
        ]

        return jsonify({'materias_con_profesores': materias_con_profesores})
