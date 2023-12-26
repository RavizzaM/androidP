from flask_restful import Resource, abort
from config import db
from app import db
from flask import jsonify, request
from sqlalchemy.sql import text

class NotasVistaProfesor(Resource):
   def post(self):
        try:
            data = request.get_json()

            ProfesorID = data['ProfesorID']
            result = db.session.execute(text("EXEC Notas_Vista_Profesor :ProfesorID"), {"ProfesorID": ProfesorID})
            notas = result.fetchall()
        except Exception as e:
            print(e)
            abort(500, description="Error del servidor")

        if notas:
            listnotas = []
            for nota in notas:
                listnotas.append({"Calificacion": nota[0], "Fecha": nota[1], "Nombre": nota[2], "Apellido": nota[3], "NombreMateria": nota[4]})
            return jsonify(listnotas)
        else:
            abort(404, description="No existen notas")