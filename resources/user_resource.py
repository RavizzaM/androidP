from app import db
from flask import jsonify, request
from flask_restful import Resource, reqparse
from models.user import User

class LoginResource(Resource):
    
    def post(self):
        data = request.get_json()

        correoelectronico = data['correoelectronico']
        contrasena = data['contrasena']

        # Verify user credentials in the database
        user = User.query.filter_by(CorreoElectronico=correoelectronico).one_or_none()
        #result = db.session.execute('EXEC sp_get_users :CorreoElectronico', {'CorreoElectronico': correoelectronico})
        #user = result.fetchall()
        if user and user.Contrasena == contrasena:
            user = user.to_json()
            return jsonify(user)
        else:
            return jsonify({'message': 'Invalid credentials'})
        

        
