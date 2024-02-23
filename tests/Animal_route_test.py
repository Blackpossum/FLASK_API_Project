import pytest
from app.utils.database import db
from app.models.animals import animals
from app.routes.Animal_management import animals_Blueprint

# siapa tau kepake , format salah 

# def test_get_animals(client):
#     # Add some sample animals to the database
#     sample_animals = [
#         {'name': 'Lion', 'latin_name': 'Panthera leo', 'kingdom_class': 'Mammalia', 'type_of_food': 'Carnivore'},
#         {'name': 'Elephant', 'latin_name': 'Loxodonta africana', 'kingdom_class': 'Mammalia', 'type_of_food': 'Herbivore'}
#     ]
#     for animal_data in sample_animals:
#         animal = animals(**animal_data)
#         db.session.add(animal)
#     db.session.commit()

#     # Send a GET request to retrieve animals
#     response = client.get('/Animal/')
#     assert response.status_code == 200

#     # Check if the response contains the expected data
#     data = response.json
#     assert len(data) == len(sample_animals)
#     assert data[0]['name'] == 'Lion'
#     assert data[1]['name'] == 'Elephant'

def test_get_animals(client):
    with client.application.app_context():
        # Adding sample animals to database
        sample_animals = [
            {'name': 'Lion', 'latin_name': 'Panthera leo', 'kingdom_class': 'Mammalia', 'type_of_food': 'Carnivore'},
            {'name': 'Elephant', 'latin_name': 'Loxodonta africana', 'kingdom_class': 'Mammalia', 'type_of_food': 'Herbivore'}
        ]
        for animal_data in sample_animals:
            animal = animals(**animal_data)
            db.session.add(animal)
        db.session.commit()

        # Send a GET request 
        response = client.get('/')
        assert response.status_code == 200

        # Check if the response 
        data = response.json
        assert len(data) == len(sample_animals)
        assert data[0]['name'] == 'Lion'
        assert data[1]['name'] == 'Elephant'

@pytest.fixture
def test_create_animal(client):
    # Send a POST request to create a new animal
    new_animal_data = {
        'name': 'Tiger',
        'latin_name': 'Panthera tigris',
        'kingdom_class': 'Mammalia',
        'type_of_food': 'Carnivore'
    }
    response = client.post('/', json=new_animal_data)
    assert response.status_code == 200

    # Check if new animal was added
    created_animal = animals.query.filter_by(name='Tiger').first()
    assert created_animal is not None

@pytest.fixture
def test_update_animal(client):
    # add sample animal to database
    sample_animal = animals(name='Lion', latin_name='Panthera leo', kingdom_class='Mammalia', type_of_food='Carnivore')
    with client.application.app_context():
        db.session.add(sample_animal)
        db.session.commit()

    update_data = {
        'name': 'Lioness',
        'latin_name': 'Panthera leo',
        'kingdom_class': 'Mammalia',
        'type_of_food': 'Carnivore'
    }
    response = client.put('/1', json=update_data)
    assert response.status_code == 200

    updated_animal = animals.query.filter_by(name='Lioness').first()
    assert updated_animal is not None

@pytest.fixture
def test_delete_animal(client):
    sample_animal = animals(name='Elephant', latin_name='Loxodonta africana', kingdom_class='Mammalia', type_of_food='Herbivore')
    db.session.add(sample_animal)
    db.session.commit()

    # Send a DELETE request 
    response = client.delete('/1')
    assert response.status_code == 200
    deleted_animal = animals.query.filter_by(name='Elephant').first()
    assert deleted_animal is None