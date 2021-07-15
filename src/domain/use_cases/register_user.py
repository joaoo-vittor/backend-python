from abc import ABC, abstractclassmethod
from src.domain.models import Users
from typing import Dict


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Case"""

        raise Exception("should implement method: register")
