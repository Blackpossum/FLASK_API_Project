from flask import Blueprint,jsonify,request
from app.utils.database import db
from app.models.feeding import feeding_schedule


feeding_Blueprint = Blueprint('feeding schedule', __name__)

# list all feedings schedule data
@feeding_Blueprint.route("/", methods=["GET"])
def get_all_feedings():
    try:
        feedings = feeding_schedule.query.all()

        serialized_feedings = []
        for feeding in feedings:
            serialized_feedings.append({
                'no': feeding.no,
                'animal_id': feeding.animal_id,
                'food_types': feeding.food_types,
                'feeding_times':feeding.feeding_times.strftime('%Y-%m-%d %H:%M:%S'),
            })

        return jsonify(serialized_feedings), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# list feeding schedule data by id 
@feeding_Blueprint.route("/<int:id>", methods=["GET"])
def get_feedings(id):
    feedings = feeding_schedule.query.get(id)
    if feedings:
        return jsonify(feedings.serialize()) , 200
    else:
        return jsonify('error feedings schedule not found'), 404
    
# create new feeding schedule
@feeding_Blueprint.route("/", methods=["POST"])
def create_feedings():
    data = request.json
    new_feedings = feeding_schedule(**data)
    db.session.add(new_feedings)
    db.session.commit()
    return jsonify({'message': 'new Feedings Schedule is succesfully added'}), 201

# update feeding_schedule
@feeding_Blueprint.route("/<int:id>", methods=["PUT"])
def update_feedings():
    try:
        data = request.json
        feeding = feeding_schedule.query.get(id)

        if feeding:
            for key, value in data.items():
                setattr(feeding,key,value)
            
            db.session.commit()
            return jsonify({"message" : "Feeding Schedule update succesfully"}) , 200
        else:
            return jsonify({"message" : "Feeding schedule not found"}) ,400
    except Exception as e:
        return str(e), 500

# Delete feeding Schedule
@feeding_Blueprint.route("/<int:id>", methods=["DELETE"])
def delete_feedings():
    try:
        feedings = feeding_schedule.query.get(id)

        if feedings:
            db.session.delete(feedings)
            db.session.commit()
            return jsonify({"message" : "Feeding Schedule deleted succesfully"}), 200
        else:
            return jsonify({"message" : "cannot find designated feeding schedule"}), 404
    except Exception as e:
        return str(e), 500
