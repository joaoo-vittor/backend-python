import enum

from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalsTypes(enum.Enum):
    """Defining Anymals Types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalsTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"

    def __eq__(self, o: object) -> bool:
        if (
            self.id == o.id
            and self.name == o.name
            and self.specie == o.specie
            and self.age == o.age
            and self.user_id == o.user_id
        ):
            return True
        return False
