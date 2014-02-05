from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

#make with the flaskings
app = Flask(__name__)

#load config
app.config.from_object('config')

#open db conection
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)
