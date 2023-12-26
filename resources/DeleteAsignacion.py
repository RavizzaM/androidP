from models.InsertAlumns import Asignaciones
from flask import jsonify, request, abort
from app import db
from flask_restful import Resource, reqparse

class DeleteAsignaciones(Resource):
    def delete(self):
        data = request.get_json()

        ProfesorID = data['ProfesorID']
        AlumnoID = data['AlumnoID']
        MateriaID = data['MateriaID']

        asignacion = Asignaciones.query.filter(
        (Asignaciones.ProfesorID == ProfesorID) &
        (Asignaciones.AlumnoID == AlumnoID) &
        (Asignaciones.MateriaID == MateriaID)
        ).first()

        
        if asignacion :
            try:
                db.session.delete(asignacion)
                db.session.commit()
                return jsonify({'Message': 'Asignacion eliminada Correctamente!'})
            except Exception as e:
                db.session.rollback()
                abort(404, description=[f'Exception error you can check log at', f'exception: {e}'])
        else:
            abort(404, description="Asignacion no encontrada!")