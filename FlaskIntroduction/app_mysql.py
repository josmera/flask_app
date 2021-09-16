from flask import Flask, render_template, url_for, request, redirect
import pymysql.cursors


app = Flask(__name__)
#
# Parametros de configuracion de la base de datos
#
# Conectar a la base de datos
connection = pymysql.connect(host='127.0.0.1',
                              user='root',
                              password='helloworld',
                              database='testapp',
                              cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.json and 'content' in request.json:
            task_content = request.json.get('content',"")
        else:
            task_content = request.form['content']
        #
        # Se crea un objeto conforme al modelo declarado
        #
        with connection:
           with connection.cursor() as cursor:
               # Crear una nueva tarea
               sql = "INSERT INTO users (content) VALUES (%s)"
               cursor.execute(sql, (task_content,))
               connection.commit()
               return redirect('/')
    else:
#        with connection.cursor() as cursor:
            # Leer un registro de la base de datos
#            sql = "SELECT content FROM users"
        cursor.execute(sql)
        tasks = cursor.fetchone()
        return render_template('index_11.html', task=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=tasks)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
