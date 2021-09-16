from flask import Flask, render_template, url_for, request, redirect
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
       # Funcion que devuelve una cadena cada vez que se crea un nuevo elemento
       # Devuelve el 'id' de la tarea recien creada
       #
       def __repr__(self):
           return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
       if request.method == 'POST':
          task_content = request.form['content']
          #
          # Se crea un objeto conforme al modelo declarado
          #
          new_task = Todo(content = task_content)
          try:
                   db.session.add(new_task)
                   db.session.commit()
                   return redirect('/')
          except:
                   return 'There was an issue adding your task'
       else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template('index_9.html', tasks=tasks)

if __name__ == "__main__":
      app.run(host='0.0.0.0',debug=True)
