from flask import Blueprint, jsonify,request
from app.utils.database import db
from app.models.animals import animals

animals_Blueprint = Blueprint('Animal end point', __name__)

# get list of animal in animals table database
@animals_Blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        animals_list = animals.query.all()

    # serialize ke json agar bisa terbaca 
        serialized_animals = []
        for animal in animals_list:  # Renaming loop variable
            serialized_animals.append({
                'id': animal.id,
                'name': animal.name,
                'latin_name': animal.latin_name,
                'kingdom_class': animal.kingdom_class,
                'type_of_food': animal.type_of_food,
            })
        return jsonify(serialized_animals),200
    except Exception as e:
        return "An error occurred while processing the request", 500



# create new animal using POST method 
@animals_Blueprint.route("/", methods=["POST"])
def create_newAnimals():
    try:
        data = request.json
        newAnimals = animals()
        newAnimals.name = data['name']
        newAnimals.latin_name = data['latin_name']
        newAnimals.kingdom_class = data['kingdom_class']
        newAnimals.type_of_food = data['type_of_food']
        db.session.add(newAnimals)
        db.session.commit()
        return 'New Animal have been added',200
    except Exception as e:
        return str(e), 500

# update animals in the zoo
@animals_Blueprint.route("/<int:id>", methods=["PUT"])
def update_animal(id):
    try:
        data = request.json
        animal = animals.query.id.get(id)
        if animal:
            animal.name = data.get('name',animal.name)
            animal.latin_name = data.get('latin_name', animal.latin_name)
            animal.kingdom_class = data.get('kingdom_class', animal.kingdom_class)
            animal.type_of_food = data.get('type_of_food', animal.type_of_food)
            db.session.comit()
            return 'Animal data update succesfully',200
        else:
            return 'designated animal not found',404
    except Exception as e:
        return str(e),500

# deleted animal in the zoo list 
@animals_Blueprint.route("/<int:id>", methods=["DELETE"])
def delete_animal(id):
    try:
        animal = animals.query.id.get(id)
        if animal:
            db.session.delete(animal)
            db.session.comit()
            return 'Animal deleted succesfully',200
        else:
            return 'designated animal not found',404
    except Exception as e:
        return str(e),500
