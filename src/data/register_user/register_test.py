from faker import Faker
from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_register():
    """Testing registry method"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repository.insert_user_params["name"] == attributes["name"]
    assert user_repository.insert_user_params["password"] == attributes["password"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method in fail"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {"name": faker.random_number(digits=5), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repository.insert_user_params == {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
