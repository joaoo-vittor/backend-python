from faker import Faker
from .find import FindPet
from src.infra.test import PetRepositorySpy

faker = Faker()


def test_by_pet_id():
    """Testing method by_pet_id"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing inputs
    assert pet_repository.select_pet_params["pet_id"] == attributes["pet_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_fail():
    """Testing method by_pet_id Fail"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"pet_id": "Hello World!!!"}
    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing inputs
    assert pet_repository.select_pet_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """Testing method by_user_id"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(user_id=attributes["user_id"])

    # Testing inputs
    assert pet_repository.select_pet_params["user_id"] == attributes["user_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id_fail():
    """Testing method by_user_id Fail"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"user_id": "Hello World!!!"}
    response = find_pet.by_pet_id(pet_id=attributes["user_id"])

    # Testing inputs
    assert pet_repository.select_pet_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_pet_id_and_user_id():
    """Testing method by_pet_id_and_user_id"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # Testing inputs
    assert pet_repository.select_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repository.select_pet_params["user_id"] == attributes["user_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id_fail():
    """Testing method by_pet_id Fail"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"pet_id": "Hello World!!!", "user_id": "olá mundo!!!"}
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # Testing inputs
    assert pet_repository.select_pet_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
