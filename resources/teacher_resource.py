from app import db
from flask import jsonify, request
from flask_restful import Resource, reqparse,abort
from models.teacher import Teacher
from sqlalchemy.sql import text

class TeacherGetMateriasResource(Resource):

    def post(self):
        data = request.get_json()

        UserID = data['UserID']
        print(UserID)
        result = db.session.execute(text("EXEC ObtenerMateriasPorProfesor :UserID"), {"UserID": UserID})
        materias = result.fetchall()
        print(materias)
        if materias:
            #user = user.to_json()
            listmaterias = []
            for materia in materias:
                listmaterias.append({"IDMateria":materia[0], "NombreMateria": materia[1], "ProfesorID":materia[2]})
            print(listmaterias)
            return jsonify(listmaterias)
        else:
            abort(404, description="Invalid credentials")
