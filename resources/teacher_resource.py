from app import db
from flask import jsonify, request
from flask_restful import Resource, reqparse
from models.teacher import Teacher
from sqlalchemy.sql import text

class TeacherGetMateriasResource(Resource):

    def post(self):
        data = request.get_json()

        UserID = data['UserID']
        print(UserID)
        result = db.session.execute(text("EXEC sp_get_materias :UserID"), {"UserID": UserID})
        materias = result.fetchall()
        print(materias)
        if materias:
            #user = user.to_json()
            listmaterias = []
            for materia in materias:
                listmaterias.append({"ProfesorID":materia[0], "NombreMateria": materia[1]})
            print(listmaterias)
            return jsonify(listmaterias)
        else:
            return jsonify({'message': 'Invalid credentials'})