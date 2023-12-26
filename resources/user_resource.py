from app import db
from flask import jsonify, request, abort
from flask_restful import Resource
from models.user import User
from hashlib import sha256
class LoginResource(Resource):
    
    def post(self):
        data = request.get_json()

        correoelectronico = data['correoelectronico']
        contrasena = data['contrasena']

        # Verifica si el usuario existe en la base de datos
        user = User.query.filter_by(CorreoElectronico=correoelectronico).one_or_none()

        if user:
            # Calcula el hash de la contraseña proporcionada por el usuario
            hashed_password = sha256(contrasena.encode()).digest()

            # Obtén el hash almacenado en la base de datos
            stored_password = user.Contrasena
            print(user.Contrasena)
            print(user.Contrasena.hex())
            print(contrasena)
            print(hashed_password)
            # Compara el hash generado con el almacenado en la base de datos
            if hashed_password == stored_password:
                # Serializa los datos del usuario a un diccionario
                user_data = user.to_json()
                return jsonify(user_data)

        # Si el usuario no existe o la contraseña es incorrecta, devuelve un error
        abort(404, description="Invalid credentials")







        
