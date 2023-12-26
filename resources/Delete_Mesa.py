from models.InsertMesa import Mesas
from flask import jsonify, request, abort
from app import db
from flask_restful import Resource, reqparse
from datetime import datetime

class DeleteMesas(Resource):
    def delete(self):
        data = request.get_json()

        ProfesorID = data['ProfesorID']
        MateriaID = data['MateriaID']
        Fecha = datetime.strptime(data['Fecha'], '%d-%m-%Y')  # Convertir la cadena a DateTime

        mesa = Mesas.query.filter(
            (Mesas.ProfesorID == ProfesorID) &
            (Mesas.MateriaID == MateriaID) &
            (Mesas.Fecha == Fecha)
        ).first()

        if mesa:
            try:
                db.session.delete(mesa)
                db.session.commit()
                return jsonify({'Message': 'Mesa eliminada Correctamente!'})
            except Exception as e:
                db.session.rollback()
                abort(404, description=[f'Exception error you can check log at', f'exception: {e}'])
        else:
            abort(404, description="Mesa no encontrada!")
