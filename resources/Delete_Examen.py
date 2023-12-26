from models.Examenes import Examenes
from flask import jsonify, request, abort
from app import db
from flask_restful import Resource, reqparse
from datetime import datetime

class DeleteExamen(Resource):
    def delete(self):
        data = request.get_json()

        AlumnoID = data['AlumnoID']
        MateriaID = data['MateriaID']
        ProfesorID = data['ProfesorID']
        Fecha = datetime.strptime(data['Fecha'], '%Y-%m-%d')  # Convertir la cadena a DateTime
        Calificacion = data['Calificacion']

        examen = Examenes.query.filter(
            (Examenes.AlumnoID == AlumnoID) &
            (Examenes.MateriaID == MateriaID) &
            (Examenes.ProfesorID == ProfesorID) &
            (Examenes.Fecha == Fecha)&
            (Examenes.Calificacion == Calificacion) 
            
        ).first()

        if examen:
            try:
                db.session.delete(examen)
                db.session.commit()
                return ({'Message': 'Examen eliminado Correctamente!'})
            except Exception as e:
                db.session.rollback()
                abort(404, description=[f'Exception error you can check log at', f'exception: {e}'])
        else:
            abort(404, description="Examen no encontrado!")