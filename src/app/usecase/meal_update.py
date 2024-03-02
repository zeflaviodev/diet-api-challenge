# pylint:disable=line-too-long,redefined-builtin
from src.domain.usecase.meal_update_interface import MealUpdateInterface, InputMealUpdate, OutputMealUpdate
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal

class MealUpdate(MealUpdateInterface):

    def __init__(self, repository: MealRepositoryInterface):
        self.repository = repository

    def execute(self, id: int, input_meal_update: InputMealUpdate) -> OutputMealUpdate:

        meal = Meal(
            name=input_meal_update.name,
            description=input_meal_update.description,
            meal_at=input_meal_update.meal_at,
            in_diet=input_meal_update.in_diet
        )

        meal_updated = self.repository.update(id, meal)

        return OutputMealUpdate(
            id=meal_updated.id,
            name=meal_updated.name,
            description=meal_updated.description,
            meal_at=meal_updated.meal_at,
            in_diet=meal_updated.in_diet
        )
