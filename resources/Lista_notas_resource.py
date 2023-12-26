from app import db
from flask import jsonify, request
from flask_restful import Resource, reqparse,abort
from sqlalchemy.sql import text


class ListaMateriasNotasbyUser(Resource):

    def post(self):
        data = request.get_json()

        UserID = data['UserID']
        print(UserID)
        result = db.session.execute(text("EXEC ObtenerExamenPorUserID :UserID"), {"UserID": UserID})
        nota = result.fetchall()
        print(nota)
        if nota:
            #user = user.to_json()
            listanotas = []
            for notas in nota:
                listanotas.append({"NombreMateria":notas[0], "Descripcion": notas[1], "Calificacion":notas[2],"Fecha": notas[3]})
            print(listanotas)
            return jsonify(listanotas)
        else:
            abort(404, description="Invalid credentials")