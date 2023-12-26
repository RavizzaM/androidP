from flask import Flask
from config import db, Config
from dotenv import load_dotenv
from flask_restful import Api


from resources.user_resource import LoginResource
from resources.teacher_resource import TeacherGetMateriasResource 
from resources.alumns_resource import AlumnsResource
from resources.insert_alumno_resource import InsertAlumnoResource 
from resources.AlumnosAsignados import AlumnosAsignadosClass 
from resources.DeleteAsignacion import DeleteAsignaciones 
from resources.insert_mesa import Insert_Mesa
from resources.Delete_Mesa import DeleteMesas
from resources.consultar_mesas import ConsultarMesasSP
from resources.Insert_Nota import Insert_Nota
from resources.Alumnos_libres import Alumnos_libres_Resource
from resources.RecuperarNotas import ObtenerNotas
from resources.Modificar_Nota import Modificar_Nota
from resources.Delete_Examen import DeleteExamen
from resources.Consultar_Materias import MateriasListas
from resources.Lista_notas_resource import ListaMateriasNotasbyUser
from resources.Consultar_Profesores import Profesoreslista
from resources.Notas_Vista_Profesor import NotasVistaProfesor
from resources.Consultar_Examenes_Calendario import Examenes


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    


    api.add_resource(LoginResource, '/login')
    api.add_resource(TeacherGetMateriasResource, '/getMaterias')
    api.add_resource(AlumnsResource, '/alumnos_sin_asignaciones/<string:apellido>')
    api.add_resource(InsertAlumnoResource, '/insertar_alumno')
    api.add_resource(AlumnosAsignadosClass, '/alumnos_asignados')
    api.add_resource(DeleteAsignaciones, '/eliminar_alumno')
    api.add_resource(Insert_Mesa, '/insertar_mesa')
    api.add_resource(DeleteMesas, '/eliminar_mesa')
    api.add_resource(ConsultarMesasSP, '/consultar_mesa')
    api.add_resource(Insert_Nota, '/insertar_nota')
    api.add_resource(Alumnos_libres_Resource, '/alumnos_libres')
    api.add_resource(ObtenerNotas,'/recuperar_notas')
    api.add_resource(Modificar_Nota,'/actualizar_nota')
    api.add_resource(DeleteExamen,'/eliminar_nota')
    api.add_resource(MateriasListas,'/Materias_con_profesores')
    api.add_resource(ListaMateriasNotasbyUser,'/Notas_alumno')
    api.add_resource(Profesoreslista, '/consultar_profesores')
    api.add_resource(NotasVistaProfesor,'/notas_vista_profesor')
    api.add_resource(Examenes,'/Recuperar_mesas_calendario')


  


    return app

# Comprueba si estás ejecutando este archivo directamente
if __name__ == "__main__":
    app = create_app()
    app.run(host='181.28.193.140')  # Asegúrate de configurar el puerto en tu Config