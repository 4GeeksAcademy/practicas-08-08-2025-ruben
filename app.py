from flask import Flask
from flask_cors import CORS
from src.routes.animal_routes import animal_bp
#python app.py
app= Flask(__name__)
CORS(app)
app.register_blueprint(animal_bp)

if  __name__ == "__main__":
    app.run(debug= True, port=5000, host="0.0.0.0")