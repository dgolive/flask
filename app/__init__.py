# importacao da pagina default
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)


# banco de dados local
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default
