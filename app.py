# archivo A (app_a.py)
import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Por defecto asume que el Service de B se llama "servicio-b" y escucha en 3000.
B_URL = os.getenv('B_URL', 'http://servicio-b:3000/api/hello')

@app.route('/', methods=['GET'])
def home():
    return 'Hola desde A', 200

@app.route('/from-b', methods=['GET'])
def from_b():
    try:
        resp = requests.get(B_URL, timeout=3)
        resp.raise_for_status()
        data = resp.json()
        return jsonify(origen='A', recibido=data), 200
    except Exception as e:
        return jsonify(error=str(e), llamando=B_URL), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
