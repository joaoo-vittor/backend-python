from src.domain.models import Pets
from src.infra.entities import Pets as PetsModels
from src.infra.config import DBConnectionHandler


class PetRepository:
    """class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Insert data in PetsEntity emtity
        :param - name: name of the pet
               - specie: Enum with specie acepted
               - age: age of the pet
               - user_id: id of the owner (FK)

        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModels(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
