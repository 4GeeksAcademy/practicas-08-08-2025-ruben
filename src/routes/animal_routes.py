from flask import Blueprint, jsonify, request
from src.models.animal import Animal

animal_bp = Blueprint("animal", __name__, url_prefix="/animal")

animals = []
next_id = 1


# @animal_bp.route("/", methods=["GET"])
# def get_animals():
#     return jsonify({"msg": "Animalico"})

def find_animal(id):
    return next((a for a in animals if a.id == id),None)



@animal_bp.route("/", methods=["GET"])
def get_animals():
    return jsonify([a.serialaizer() for a in animals])

@animal_bp.route("/", methods=["POST"])
def create_animal():
    global next_id
    data = request.get_json()
    if not isinstance(("name"),str )in data or not isinstance(("type"),str ) in data or not isinstance(("age"),int ) in data:
        return jsonify("Faltan datos por rellenar"), 400
    new_animal = Animal(
        id=next_id, name=data["name"], type=data["type"], age=data["age"]
    )
    animals.append(new_animal)
    next_id += 1
    return jsonify(new_animal.serialaizer()), 201

@animal_bp.route("/<int:id> ", methods=["GET"])
def get_animal(id):
    data = request.get_json(id)
    if data:
        return jsonify(data.serialaizer()),200
    return jsonify("Faltan id")

# @animal_bp.route("/<int:id>", methods=["PUT"])
# def 