from flask import Flask
from config import db, Config
from dotenv import load_dotenv
from flask_restful import Api

from resources.user_resource import LoginResource
from resources.teacher_resource import TeacherGetMateriasResource

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object(Config)
    #print(db.engine())
    db.init_app(app)
    api = Api(app)


    api.add_resource(LoginResource, '/login')
    api.add_resource(TeacherGetMateriasResource, '/getmaterias')


    #with app.app_context():
    #    db.create_all()

    return app