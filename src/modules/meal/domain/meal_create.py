#pylint:disable=redefined-builtin,too-many-arguments
from abc import ABC, abstractmethod
from src.modules.meal.use_case.create.meal_create_dto import InputMealCreateDto, OutputealCreateDto

class MealCreate(ABC):

    @abstractmethod
    def create_meal(self, meal_dto: InputMealCreateDto) -> OutputealCreateDto: pass
