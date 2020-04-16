from flask import Flask

app = Flask(__name__)

@app.route('/update')

def update():
    return 'Datos Actualizados'

if __name__ == '__main__':
    app.run(debug=True, port = 4000)
