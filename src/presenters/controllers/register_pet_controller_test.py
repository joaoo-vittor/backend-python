from faker import Faker
from .register_pet_controller import RegisterPetController
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attribute = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.router(HttpRequest(body=attribute))

    # testing input
    assert register_pet_use_case.registry_param["name"] == attribute["name"]
    assert register_pet_use_case.registry_param["specie"] == attribute["specie"]
    assert register_pet_use_case.registry_param["age"] == attribute["age"]
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attribute["user_information"]
    )

    # testing output
    assert response.status_code == 200
    assert "error" not in response.body
