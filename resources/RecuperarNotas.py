#EXEC RecuperarNotas @MateriaID = 4, @AlumnoID = 2, @ProfesorID = 4, @Fecha = '2023-02-11'
from flask_restful import Resource, abort
from config import db
from app import db
from flask import jsonify, request
from sqlalchemy.sql import text

class ObtenerNotas(Resource):
   def post(self):
        try:
            data = request.get_json()

            
            MateriaID = data['MateriaID']
            AlumnoID = data['AlumnoID']
            ProfesorID = data['ProfesorID']
            Fecha = data['Fecha']
            result = db.session.execute(text("EXEC RecuperarNotas :MateriaID, :AlumnoID, :ProfesorID, :Fecha"), {"MateriaID": MateriaID, "AlumnoID": AlumnoID,"ProfesorID":ProfesorID,"Fecha":Fecha})
            nota = result.fetchall()
            print(nota)
        except Exception as e:
            print(e)
            abort(500, description="Error del servidor")

        if nota:
            listnotas = []
            for notas in nota:
                print(listnotas)
                listnotas.append({"Calificacion": notas[5]})
            return jsonify(listnotas)
        else:
            abort(404, description="No existen notas")

            #"AlumnoID": notas[1],"MateriaID": notas[2],"ProfesorID": notas[3],"Fecha": notas[4],