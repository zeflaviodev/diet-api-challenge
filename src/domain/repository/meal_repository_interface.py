from abc import ABC, abstractmethod
from src.domain.entity.meal import Meal

class MealRepositoryInterface(ABC):

    @abstractmethod
    def create(self, meal: Meal) -> Meal: pass

    @abstractmethod
    def find_all(self) -> list[Meal]: pass
