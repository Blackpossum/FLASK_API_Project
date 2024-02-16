from flask import Blueprint, jsonify


Employe_blueprint = Blueprint("Employe management end point", __name__)

Employe =[

    {
    "firstName": "",
    "LastName" : "",
    "Position" : "",
    "id"       : "",
    },
        {
    "firstName": "",
    "LastName" : "",
    "Position" : "",
    "id"       : "",
    },
        {
    "firstName": "",
    "LastName" : "",
    "Position" : "",
    "id"       : "",
    },
        {
    "firstName": "",
    "LastName" : "",
    "Position" : "",
    "id"       : "",
    },
]

@Employe_blueprint.route("/", methods=["GET"])
def get_Employe():
    return jsonify(Employe)

@Employe_blueprint.route("/", methods=["POST"])
def create_Employe():
    return "Post Employe"

@Employe_blueprint.route("/<int:Employe_id>", methods=["PUT"])
def update_Employe(Employe_id):
    return str(Employe_id)

@Employe_blueprint.route("/<int:Employe_id>", methods=["DELETE"])
def delete_Employe(Employe_id):
    return str(Employe_id)