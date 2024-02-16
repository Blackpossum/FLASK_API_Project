from flask import Blueprint,jsonify


Animal_Blueprint = Blueprint('Annimal end point', __name__)

Animal = [
    {
    "id" : "001",
    "Animal" : "bengal tiger",
    "species": "mamal",
    },
        {
    "id" : "002",
    "Animal" : "Cappibara",
    "species": "mamal",
    },
    {
    "id" : "003",
    "Animal" : "Ostritch",
    "species": "bird",
    },
]

@Animal_Blueprint.route("/", methods=["GET"])
def get_Animal():
    return jsonify(Animal)

@Animal_Blueprint.route("/", methods=["POST"])
def create_zoo():
    return "post Animal"

@Animal_Blueprint.route("/<int:zoo_id>", methods=["PUT"])
def update_Animal(Animal_id):
    return str(Animal_id)

@Animal_Blueprint.route("/<int:Animal_id>", methods=["DELETE"])
def delete_Animal(Animal_id):
    return str(Animal_id)
