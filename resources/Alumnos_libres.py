from flask import jsonify, request
from flask_restful import Resource
from models.alumns import AlumnosSinAsignaciones
from config import db
import unicodedata
from sqlalchemy import text

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

class Alumnos_libres_Resource(Resource):
    def post(self):
        data = request.get_json()

        apellido = remove_accents(data.get('Apellido', '')).lower()
        materia_id = data.get('MateriaID', '')
        print(apellido)
        print(materia_id)

        if not apellido or not materia_id:
            return {'error': 'Se requieren los campos de apellido y materia_id'}, 400

        # Obtener una conexión
        conn = db.engine.connect()

        try:
            
            query = text("EXEC Alumnos_Libres @Apellido=:apellido, @MateriaID=:materia_id")

        # Obtener una conexión a la base de datos
            conn = db.engine.connect()
        
            query_result = conn.execute(query, {"apellido": apellido, "materia_id": materia_id})



            # Convertir los resultados a formato JSON
            alumnos_libres = [
                {'UserID': row.UserID, 'Nombre': row.Nombre, 'Apellido': row.Apellido,
                 'CorreoElectronico': row.CorreoElectronico, 'Tipo': row.Tipo, 'AlumnoID': row.AlumnoID}
                for row in query_result
            ]

            # Verificar si hay resultados
            if not alumnos_libres:
                return {'error': 'No se encontraron alumnos libres con el apellido y materia proporcionados'}, 404

            return jsonify({'alumnos_libres': alumnos_libres})

        finally:
            # Cerrar la conexión
            conn.close()

