from flask import jsonify
from flask_restful import Resource
from models.Examenes_Calendario import Examen_Calendario  # Importa el modelo de la vista

class Examenes(Resource):
     def get(self):
        query_result = Examen_Calendario.query.all()

        if not query_result:
            return {'error': 'No se encontraron datos en la vista'}, 404

        Examanes_Cargados = [result.to_dict() for result in query_result]

        return jsonify({'Examanes_Cargados': Examanes_Cargados})