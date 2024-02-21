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
        return jsonify(serialized_animals, 200)
    except Exception as e:
        return e, 500


# create new animal using POST method 
@animals_Blueprint.route("/", methods=["POST"])
def create_newAnimals():
    try:
        data = request.json
        print(data)
        newAnimals = animals()
        newAnimals.name = data["name"]
        newAnimals.animals_species = data["animals_species"]
        newAnimals.type_of_food = data["type_of_food"]
        db.session.add(newAnimals)
        db.session.commit()
        return 'New Animal have been added',200
    except Exception as e:
        return e, 500

# @animals_Blueprint.route("/<int:zoo_id>", methods=["PUT"])
# def update_Animal(Animal_id):
#     return str(Animal_id)

# @animals_Blueprint.route("/<int:Animal_id>", methods=["DELETE"])
# def delete_Animal(Animal_id):
#     return str(Animal_id)
