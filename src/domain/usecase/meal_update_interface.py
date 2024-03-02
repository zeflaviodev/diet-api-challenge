# pylint:disable=redefined-builtin
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from src.domain.repository.meal_repository_interface import MealRepositoryInterface

@dataclass
class InputMealUpdate():
    name: str = ''
    description: str = ''
    meal_at: datetime = None
    in_diet: bool = True


@dataclass
class OutputMealUpdate():
    id: int
    name: str
    description: str
    meal_at: datetime
    in_diet: bool


class MealUpdateInterface(ABC):

    def __init__(self, repository: MealRepositoryInterface) -> None: pass

    @abstractmethod
    def execute(self, id: int, input_meal_update: InputMealUpdate) -> OutputMealUpdate: pass
