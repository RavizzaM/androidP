from flask_restful import Resource, abort
from config import db
from app import db
from flask import jsonify, request
from sqlalchemy.sql import text

class ConsultarMesasSP(Resource):
   def post(self):
        try:
            data = request.get_json()

            ProfesorID = data['ProfesorID']
            MateriaID = data['MateriaID']
            result = db.session.execute(text("EXEC mesasSP :ProfesorID, :MateriaID"), {"ProfesorID": ProfesorID, "MateriaID": MateriaID})
            mesa = result.fetchall()
        except Exception as e:
            print(e)
            abort(500, description="Error del servidor")

        if mesa:
            listmesa = []
            for mesas in mesa:
                listmesa.append({"ProfesorID": mesas[0], "MateriaID": mesas[1], "Fecha": mesas[2]})
            return jsonify(listmesa)
        else:
            abort(404, description="No existen mesas")
