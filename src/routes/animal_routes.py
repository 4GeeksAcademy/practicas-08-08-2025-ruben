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
##
###
###


@animal_bp.route("/", methods=["GET"])
def get_animals():
    return jsonify([a.serializer() for a in animals]),200

@animal_bp.route("/", methods=["POST"])
def create_animal():
    global next_id
    data = request.get_json()
    if not isinstance(data.get("name"),str ) or not isinstance(data.get("type"),str ) or not isinstance(data.get("age"),int ):
        return jsonify("Faltan datos por rellenar"), 400
    new_animal = Animal(
        id=next_id, name=data["name"], type=data["type"], age=data["age"]
    )
    animals.append(new_animal)
    next_id += 1
    return jsonify({'msg': 'Datos guardados'},new_animal.serializer()), 201

@animal_bp.route("/<int:id> ", methods=["GET"])
def gshow_animal(id):
    for a in animals:
        if id == a.id:
            return jsonify({'msg': 'Animal encontrado'}, a.serializer()), 200
    return jsonify({'msg': 'Animal no encontrado'}), 404

@animal_bp.route('/<int:id>', methods= ['DELETE'])
def delete_animal(id):
    for a in animals:
        if id == a.id:
            animals.remove(a)
            return jsonify({'msg': 'Animal eliminado'}, a.serializer()), 200
    return jsonify({'msg': 'Animal no encontrado'}), 404

@animal_bp.route('/<int:id>', methods= ['PUT'])
def update_animal(id):
    data = request.get_json()
    for a in animals:
        if id == a.id:
            a.name = data.get("name", a.name)
            a.age = data.get("age", a.age)
            a.type = data.get("type", a.type)
            return jsonify({'msg': 'Animal modificado'}, a.serializer()), 200
    return jsonify({'msg': 'Error'}),400

