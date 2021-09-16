from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
      return render_template("index_4.html")

if __name__ == "__main__":
       app.run(host='0.0.0.0',debug=True)
