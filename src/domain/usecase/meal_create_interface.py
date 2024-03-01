from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from src.domain.repository.meal_repository_interface import MealRepositoryInterface

@dataclass
class InputMealCreate():
    name: str = ''
    description: str = ''
    meal_at: datetime = None
    in_diet: bool = True


@dataclass
class OutputMealCreate():
    id: int
    name: str
    description: str
    meal_at: datetime
    in_diet: bool


class MealCreateInterface(ABC):

    def __init__(self, repository: MealRepositoryInterface) -> None: pass

    @abstractmethod
    def execute(self, input_meal_create: InputMealCreate) -> OutputMealCreate: pass
