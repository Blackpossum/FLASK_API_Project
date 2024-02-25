import pytest 
from app.utils.database import db
from app.models.employee import employee


def test_get_employee(client_with_employees) :
    with client_with_employees.application.app_context():
        # add sample employee to database 
        sample_employe = [
            {'name': 'Bethany','age':27, 'specialization': 'zoology and environment study', 'section_operation': 'amphibious and mammalia'},
            {'name': 'Diana', 'age':30, 'specialization': 'virology and lab research', 'section_operation': 'laboratory and reaserch'}
        ]
        for employee_data in sample_employe:
            show_employee= employee(**employee_data)
            # print(employee_data)
            db.session.add(show_employee)
            db.session.commit()
        

        # sending GET request
        response = client_with_employees.get('/')
    
        # print(response)
        assert response.status_code == 200

        # response check 
        response_data = response.json
        
        #check if response matches sample employee 
        assert len(response_data) == len(sample_employe)
        assert response_data[0]['name'] == 'Bethany'
        assert response_data[1]['name'] == 'Diana'

@pytest.fixture
def test_create_emloyee(client_with_employees):
    # send POST request to create new employee
    new_employee_data = {
        'name': 'Esther',
        'age': 31,
        'specialization': 'System analyst and IT infra',
        'section_operation': 'IT division'
    }
    #  check status code 
    response = client_with_employees.post('/',json = new_employee_data)
    assert response.status_code == 200 

    # check if new employee is created
    created_employee = employee.query.filter_by(name = 'Esther').first()
    assert created_employee is not None

@pytest.fixture
def test_update_animal(client_with_employees):
    # create sample employee 
    sample_employee = employee(name='Esther', age =31, specialization='System analyst and IT infra', section_operation='IT division')
    with client_with_employees.application.app_context():
        db.session.add(sample_employee)
        db.session.commit()

    update_data = {
        'name': 'Estheriana',
        'age': 29,
        'specialization':'IT infrastructure',
        'section_operation': 'IT division',
    }

    # if error change to 1 
    response = client_with_employees.put('/0', json=update_data)
    assert response.status_code == 200

#  check if employed is updated
    update_employee = employee.query.filter_by(name = 'Estheriana').first()
    assert update_employee is not None

@pytest.fixture
def test_delete_employee(client_with_employees):
    # add a sample employee to database
    sample_employee = employee(name= 'Bethany',age=27, specialization= 'zoology and environment study', section_opertaion ='amphibious and mammalia')
    db.session.add(sample_employee)
    db.session.commit()

    # send delete request 
    response = response.delete('/1')

    # check response status code 
    assert response.status_code == 200

    # check employe is deleted
    deleted_employee = employee.query.filter_by(name='Bethany').first()
    assert deleted_employee is None


