from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal

@dataclass
class OutputMealFindAll():
    meals: List[Meal]

    def __len__(self) -> int:
        return len(self.meals)

class MealFindAllInterface(ABC):

    def __init__(self, repository: MealRepositoryInterface) -> None: pass

    @abstractmethod
    def execute(self) -> OutputMealFindAll: pass
