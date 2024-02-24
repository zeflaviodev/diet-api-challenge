from abc import ABC, abstractmethod
from src.modules.meal.domain.meal_entity import MealEntity

class MealRepository(ABC):

    @abstractmethod
    def create(self, meal: MealEntity) -> None: pass

    @abstractmethod
    def find_by_id(self, meal_id: int) -> MealEntity: pass
