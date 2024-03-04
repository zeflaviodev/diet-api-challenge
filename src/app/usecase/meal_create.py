#pylint:disable=line-too-long
from datetime import datetime
from src.domain.usecase.meal_create_interface import MealCreateInterface, InputMealCreate, OutputMealCreate
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal

class MealCreate(MealCreateInterface):

    def __init__(self, repository: MealRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, input_meal_create: InputMealCreate) -> OutputMealCreate:
        meal_at = None
        if input_meal_create.meal_at :
            meal_at = datetime.strptime(input_meal_create.meal_at, "%Y-%m-%d %H:%M")

        meal = Meal(
            name = input_meal_create.name,
            description = input_meal_create.description,
            meal_at = meal_at,
            in_diet = input_meal_create.in_diet,
        )

        new_meal = self.repository.create(meal)

        return OutputMealCreate(
            id=new_meal.id,
            name=new_meal.name,
            description=new_meal.description,
            meal_at=new_meal.meal_at.strftime("%Y-%m-%d %H:%M"),
            in_diet=new_meal.in_diet,
        )
