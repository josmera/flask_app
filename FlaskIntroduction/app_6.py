from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
#
# Parametros de configuracion a la base de datos
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
#
# A continuacion se crea un modelo o esquema para la base de datos
#
class Todo(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       content = db.Column(db.String(200), nullable=False)
       completed = db.Column(db.Integer, default=0)
       date_created = db.Column(db.DateTime, default=datetime.utcnow)
       #
       # Funcion que devuelve una cadena cada vez que se crea un nuevo elemento
       # Devuelve el 'id' de la tarea recien creada
       #
       def __repr__(self):
             return '<Task %r>' % self.id

@app.route('/')
def index():
      return render_template('index_6.html')

if __name__ == "__main__":
       app.run(host='0.0.0.0',debug=True)
