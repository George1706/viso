#Dependencia de flask
from flask import Flask,render_template
#Dependencia de configuración
from .config import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

#Configuracion objeto flask
app.config.from_object(Config)

#Crear el objetto de Moldelos
db = SQLAlchemy(app)

#Crear objeto de migración
migrate = Migrate(app,db)

#importar los modelos  de .models
from .models import Producto,Usuario,Cliente,Venta,Administrador