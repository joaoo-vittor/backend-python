from src.infra.repo import PetRepository
from src.data.find_pet import FindPet
from src.presenters.controllers import FindPetController


def find_pet_composer() -> FindPetController:
    """Composing Find Pet Route
    :param - None
    :return - Object with Find Pet Route
    """

    repository = PetRepository()
    find_pet_use_case = FindPet(repository)
    find_pet_route = FindPetController(find_pet_use_case)

    return find_pet_route
