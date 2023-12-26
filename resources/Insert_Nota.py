from flask_restful import Resource, reqparse
from config import db
from models.InsertNota import Notas
from models.InsertAlumns import Asignaciones
from datetime import datetime, timedelta
class Insert_Nota(Resource):
    def post(self):
        
        # Analizador de solicitudes para obtener los datos del cuerpo de la solicitud
        parser = reqparse.RequestParser()
        parser.add_argument('AlumnoID', type=int, required=True)
        parser.add_argument('MateriaID', type=int, required=True)
        parser.add_argument('ProfesorID', type=int, required=True)
        parser.add_argument('Fecha', type=str, required=True)
        parser.add_argument('Calificacion', type=int, required=True)
        args = parser.parse_args()
        #print(args)

        # Convertir la cadena de fecha en un objeto 'datetime'
        fecha_str = args['Fecha']
        fecha_datetime = datetime.strptime(fecha_str, f"%d-%m-%Y")  # Convertir a datetime
        #fecha_datetime = datetime.combine(args['Fecha'], datetime.min.time()).__str__
        print(fecha_datetime)
        print(type(fecha_datetime))

        # Definir un rango de fechas para buscar notas existentes (mismo día)
        fecha_inicio = fecha_datetime.replace(hour=0, minute=0, second=0)
        fecha_fin = fecha_datetime.replace(hour=23, minute=59, second=59)
        

       # Verificar si ya existe una nota para ese alumno, materia y profesor en el rango de fechas del día
        existing_nota = Notas.query.filter(
            Notas.AlumnoID == args['AlumnoID'],
            Notas.MateriaID == args['MateriaID'],
            Notas.ProfesorID == args['ProfesorID'],
            Notas.Fecha.between(fecha_inicio, fecha_fin)
        ).first()

        if existing_nota:
            return {'error': 'La Nota ya existe'}, 400

     
        nota = Notas(
            AlumnoID=args['AlumnoID'],
            MateriaID=args['MateriaID'],
            ProfesorID=args['ProfesorID'],
            Fecha=fecha_datetime,
            Calificacion=args['Calificacion']
        )

        db.session.add(nota)
        db.session.commit()

        return {'message': 'Nota asignada exitosamente'}, 201