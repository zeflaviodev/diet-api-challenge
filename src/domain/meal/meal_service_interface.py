from abc import ABC, abstractmethod
from typing import Dict
from src.domain.meal.meal_entity import MealEntity

class MealServiceInterface(ABC):

    @abstractmethod
    def find(self) -> Dict: pass

    @abstractmethod
    def create(self, new_meal: MealEntity) -> None: pass
