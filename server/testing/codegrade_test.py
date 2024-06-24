from server.app import app, db
from models import Pet  # Assuming Pet model is defined in models.py
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_pet_model(client):
    # Create a Pet object and add it to the database
    pet = Pet(name='Fluffy', species='Cat')
    db.session.add(pet)
    db.session.commit()

    # Retrieve the pet from the database
    retrieved_pet = Pet.query.filter_by(name='Fluffy').first()

    # Assert that the retrieved pet matches the original pet
    assert retrieved_pet is not None
    assert retrieved_pet.name == 'Fluffy'
    assert retrieved_pet.species == 'Cat'

def test_add_pet(client):
    # Send a POST request to add a new pet
    response = client.post('/add_pet', json={'name': 'Rex', 'species': 'Dog'})

    # Check if the pet was added successfully
    assert response.status_code == 201  # Assuming 201 indicates successful creation

    # Retrieve the newly added pet from the database
    new_pet = Pet.query.filter_by(name='Rex').first()

    # Assert that the new pet exists and has correct attributes
    assert new_pet is not None
    assert new_pet.name == 'Rex'
    assert new_pet.species == 'Dog'
