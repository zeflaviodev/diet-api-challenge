#pylint:disable=redefined-builtin,too-many-arguments
from abc import ABC, abstractmethod
from datetime import datetime

from src.modules.meal.domain.meal_entity import MealEntity

class MealCreate(ABC):

    @abstractmethod
    def create_meal(self,
        id: int,
        name: str = '',
        description: str = '',
        meal_at: datetime = datetime.now(),
        in_diet: bool = True) -> MealEntity:
        pass
