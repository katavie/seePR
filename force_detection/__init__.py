from . import pressure

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

values = []

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return("<h1>About Page<h1>")
    return(x)

@app.route("/data")
def data():
    return '''
    <script>
    const Http = new XMLHttpRequest();
    const url='http://localhost:5000/sensor';

    while(true){
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange=(e)=>{
    console.log(Http.responseText)

    }
    }

    </script>



    '''


@app.route("/sensor")
def sensor():
    return(values[-1])


@app.route("/startsensor")
def startsensor():
    while True:
        values.append(pressure.get_sensor_data())

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
