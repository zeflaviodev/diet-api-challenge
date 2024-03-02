from abc import ABC, abstractmethod
from src.domain.repository.meal_repository_interface import MealRepositoryInterface

class MealDeleteInterface(ABC):

    def __init__(self, repository: MealRepositoryInterface) -> None: pass

    @abstractmethod
    def execute(self) -> None: pass
