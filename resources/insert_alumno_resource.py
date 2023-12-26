from flask_restful import Resource, reqparse
from config import db
from models.alumns import AlumnosSinAsignaciones
from models.InsertAlumns import Asignaciones

class InsertAlumnoResource(Resource):
    def post(self):
        # Analizador de solicitudes para obtener los datos del cuerpo de la solicitud
        parser = reqparse.RequestParser()
        parser.add_argument('ProfesorID', type=int, required=True)
        parser.add_argument('AlumnoID', type=int, required=True)
        parser.add_argument('MateriaID', type=int, required=True)
        args = parser.parse_args()

        # Verificar si ya existe una asignación con esos valores
        existing_assignment = Asignaciones.query.filter_by(
            ProfesorID=args['ProfesorID'],
            AlumnoID=args['AlumnoID'],
            MateriaID=args['MateriaID']
        ).first()

        if existing_assignment:
            return {'error': 'La asignación ya existe'}, 400

        # Crear una nueva asignación y guardarla en la base de datos
        asignacion = Asignaciones(
            ProfesorID=args['ProfesorID'],
            AlumnoID=args['AlumnoID'],
            MateriaID=args['MateriaID']
        )

        db.session.add(asignacion)
        db.session.commit()

        return {'message': 'Alumno Agregado exitosamente'}, 201

