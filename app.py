from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
import time
import db_functions as db

app = Flask(__name__)

start = time.perf_counter()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        stop = time.perf_counter() - start
        db.insert_time(str(stop))
        return redirect(
            url_for(
                'hello',
                name=name,
                surname=surname,
                stop=str(stop)))
    return render_template("index.html")


@app.route('/hello?<name>?<surname>?<stop>')
def hello(name, surname, stop):
    return render_template(
        'hello.html',
        values=(
            name,
            surname,
            str(stop),
            db.avarage_time()))


if __name__ == '__main__':
    app.run(debug=True)
