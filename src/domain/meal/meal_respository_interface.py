from abc import ABC, abstractmethod
from typing import Dict
from src.domain.meal.meal_entity import MealEntity

class MealRepositoryInterface(ABC):

    @abstractmethod
    def create_meal(self, meal: MealEntity) -> Dict: pass

    @abstractmethod
    def get_meal_by_id(self, meal_id: int) -> MealEntity: pass
