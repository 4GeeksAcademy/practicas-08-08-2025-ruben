# practicas-08-08-2025-ruben

repositorio
crear el entorno virtual con python -m venv venv
para activar
. ./venv/bin/activate
instalar fask
pip install flask fask-cors

crear app.py
y escribir :

from flask import Flask
from flask_cors import CORS
from src.routes.animal_routes import animal_bp
#python app.py
app= Flask(__name__)
CORS(app)
app.register_blueprint(animal_bp)

if  __name__ == "__main__":
    app.run(debug= True, port=5000, host="0.0.0.0")




frontend :
npm create vite@latest
si piden nombre del package 
package.json
