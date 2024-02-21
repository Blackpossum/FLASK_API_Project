from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employee import employee

employee_Blueprint = Blueprint("Employee management end point", __name__)

@employee_Blueprint.route("/", methods=["GET"])
def get_employee():
    try:
        Employee_list = employee.query.all()
        serialized_Employee = []
        for employe in Employee_list:
            serialized_Employee.append({
                'id': employe.id,
                'name': employe.name,
                'age': employe.age,
                'specialization': employe.specialization,
                'section_operation': employe.section_operation,
            })
        return jsonify(serialized_Employee), 200
    except Exception as e:
        return str(e), 500

@employee_Blueprint.route("/", methods=["POST"])
def create_employee():
    try:
        data = request.json
        Newemployee = employee(
            name=data['name'],
            age=data['age'],
            specialization=data['specialization'],
            section_operation=data['section_operation']
        )
        db.session.add(Newemployee)
        db.session.commit()
        return 'New Employee data has been added', 200
    except Exception as e:
        return str(e), 500

@employee_Blueprint.route("/<int:id>", methods=["PUT"])
def update_employee(id):
    try:
        data = request.json
        employe = employee.query.get(id)
        if employe:
            employe.name = data.get('name', employe.name)
            employe.age = data.get('age', employe.age)
            employe.specialization = data.get('specialization', employe.specialization)
            employe.section_operation = data.get('section_operation', employe.section_operation)
            db.session.commit()
            return 'Employee data successfully edited', 200
        else:
            return 'Employee data not found', 404
    except Exception as e:
        return str(e), 500

@employee_Blueprint.route("/<int:id>", methods=["DELETE"])
def delete_employee(id):
    try:
        employe = employee.query.get(id)
        if employe:
            db.session.delete(employe)
            db.session.commit()
            return 'Employee data deleted successfully', 200
        else:
            return 'Designated Employee data not found', 404
    except Exception as e:
        return str(e), 500
