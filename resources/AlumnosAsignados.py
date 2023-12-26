from app import db
from flask import jsonify, request
from flask_restful import Resource, reqparse,abort
from models.teacher import Teacher
from sqlalchemy.sql import text

class AlumnosAsignadosClass(Resource):

    def post(self):
        try:
            data = request.get_json()

            ProfesorID = data['ProfesorID']
            MateriaID = data['MateriaID']
            print(ProfesorID)
            print(MateriaID)
            result = db.session.execute(text("EXEC ObtenerAlumnosPorProfesorID :ProfesorID, :MateriaID"), {"ProfesorID": ProfesorID, "MateriaID": MateriaID})
            alumnos = result.fetchall()
            print(alumnos)
        except Exception as e:
            print(e)
        if alumnos:
            #user = user.to_json()
            listalumnos = []
            for alumno in alumnos:
                listalumnos.append({"Nombre":alumno[1], "Apellido": alumno[2], "CorreoElectronico":alumno[3], "AlumnoID": alumno[6]})
            print(listalumnos)
            return jsonify(listalumnos)
        else:
            abort(404, description="Invalid credentials")
