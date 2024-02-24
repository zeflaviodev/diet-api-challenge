#pylint:disable=line-too-long
from src.modules.meal.use_case.create.meal_create_use_case import MealCreateUseCase
from src.modules.meal.infrastructure.repositories.meal_repository import MealRepository
from src.modules.meal.infrastructure.controllers.create.meal_create_controller import MealCreateController

def meal_create_presenter():
    repository = MealRepository()
    use_case = MealCreateUseCase(repository)
    controller = MealCreateController(use_case)

    return controller.handle
