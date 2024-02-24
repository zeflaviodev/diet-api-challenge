from datetime import datetime
from src.modules.meal.use_case.create.meal_create_use_case import MealCreateUseCase
from src.modules.meal.infrastructure.repositories.meal_repository import MealRepository
from .meal_create_controller import MealCreateController

class HttpCreateRequestMock():
    def __init__(self):
        self.body = {
            "name": "name",
            "description": "description",
            "meal_at": datetime.now(),
            "in_diet": True
        }

def test_meal_controller_create():
    http_request_mock = HttpCreateRequestMock()

    repository = MealRepository()

    meal_create_use_case = MealCreateUseCase(repository)

    meal_controller = MealCreateController(meal_create_use_case)

    meal_controller.handle(http_request_mock)
    # meal_controller = MealController()

    # meal_controller.create(http_request_mock)


# test_meal_controller_create()
