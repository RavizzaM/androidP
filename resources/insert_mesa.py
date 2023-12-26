from flask_restful import Resource, reqparse
from config import db
from models.InsertMesa import Mesas
from datetime import datetime
from models.InsertAlumns import Asignaciones

class Insert_Mesa(Resource):
    def post(self):
        
        # Analizador de solicitudes para obtener los datos del cuerpo de la solicitud
        parser = reqparse.RequestParser()
        parser.add_argument('MateriaID', type=int, required=True)
        parser.add_argument('ProfesorID', type=int, required=True)
        parser.add_argument('Fecha', type=str, required=True)
        args = parser.parse_args()
        print(args)

        # Convertir la cadena de fecha en un objeto 'datetime'
        fecha_str = args['Fecha']
        fecha_datetime = datetime.strptime(fecha_str, f"%d-%m-%Y")  # Convertir a datetime
        print(fecha_datetime)
        print(type(fecha_datetime))

        # Verificar si ya existe 
        existing_mesa = Mesas.query.filter_by(
            MateriaID=args['MateriaID'],
            ProfesorID=args['ProfesorID'],
            Fecha=fecha_datetime.date()  # Obtener solo la parte de la fecha
        ).first()

        if existing_mesa:
            return {'error': 'La Mesa ya existe'}, 400

     
        mesa = Mesas(
            MateriaID=args['MateriaID'],
            ProfesorID=args['ProfesorID'],
            Fecha=fecha_datetime  # Usar el objeto datetime
        )

        db.session.add(mesa)
        db.session.commit()

        return {'message': 'Mesa creada exitosamente'}, 201

