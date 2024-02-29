import pytest
from app.utils.database import db
from app.models.animals import animals
from app.routes.Animal_management import animals_Blueprint


sample_animals = [
    { 'id':1 ,'name': 'Lion', 'latin_name': 'Panthera leo', 'kingdom_class': 'Mammalia', 'type_of_food': 'Carnivore'},
    {'id':2 ,'name': 'Elephant', 'latin_name': 'Loxodonta africana', 'kingdom_class': 'Mammalia', 'type_of_food': 'Herbivore'}
]

def test_get_animals(client_with_animals):
    with client_with_animals.application.app_context():
        # Adding sample animals to database
        for animal_data in sample_animals:
            animal = animals(**animal_data)
            db.session.add(animal)
        db.session.commit()

        # Send a GET request 
        response = client_with_animals.get('/')
        assert response.status_code == 200

        # Check if the response 
        data = response.json
        assert len(data) == len(sample_animals)
        assert data[0]['name'] == 'Lion'
        assert data[1]['name'] == 'Elephant'


def test_create_animal(client_with_animals):
    with client_with_animals.application.app_context():
        # Send a POST request to create a new animal
        new_animal_data = {
            'name': 'Tiger',
            'latin_name': 'Panthera tigris',
            'kingdom_class': 'Mammalia',
            'type_of_food': 'Carnivore'
        }
        response = client_with_animals.post('/', json=new_animal_data)
        assert response.status_code == 200

        # Check if new animal was added
        created_animal = animals.query.filter_by(name='Tiger').first()
        assert created_animal is not None


def test_update_animal(client_with_animals):
    with client_with_animals.application.app_context():
        # Adding a sample animal to the database
        sample_animal = animals(name='Lion', latin_name='Panthera leo', kingdom_class='Mammalia', type_of_food='Carnivore')
        db.session.add(sample_animal)
        db.session.commit()

        # Send a PUT request to update the animal
        update_data = {
            'name': 'Lioness',
            'latin_name': 'Panthera leo',
            'kingdom_class': 'Mammalia',
            'type_of_food': 'Carnivore'
        }
        response = client_with_animals.put(f'/animal/{sample_animal.name}', json=update_data)
        assert response.status_code == 200

        # Check if the animal was updated
        updated_animal = animals.query.filter_by(name='Lioness').first()
        assert updated_animal is not None
        assert updated_animal.name == 'Lioness'  # Ensure the name is updated correctly
        assert updated_animal.latin_name == 'Panthera leo'  # Ensure other attributes remain unchanged
        assert updated_animal.kingdom_class == 'Mammalia'
        assert updated_animal.type_of_food == 'Carnivore'



def test_delete_animal(client_with_animals):
    with client_with_animals.application.app_context():
        # Adding two sample animals to the database
        sample_animal1 = animals(name='Elephant', latin_name='Loxodonta africana', kingdom_class='Mammalia', type_of_food='Herbivore')
        sample_animal2 = animals(name='Tiger', latin_name='Panthera tigris', kingdom_class='Mammalia', type_of_food='Carnivore')
        db.session.add_all([sample_animal1, sample_animal2])
        db.session.commit()

        # Print the animals before deletion
        print("Before deletion:")
        print("Sample Animal 1:", sample_animal1)
        print("Sample Animal 2:", sample_animal2)

        # Send a DELETE request for the first animal by name
        response1 = client_with_animals.delete(f'/animal/{sample_animal1.name}')
        print("Response:", response1.data)
        assert response1.status_code == 200

        # Check if the first animal was deleted
        deleted_animal1 = animals.query.filter_by(name='Elephant').first()
        print("After deletion:")
        print("Deleted Animal 1:", deleted_animal1)

        assert deleted_animal1 is None
