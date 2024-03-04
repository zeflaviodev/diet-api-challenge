from src.infra.repository.db.meal_repository_db import MealRepositoryDB
from src.app.usecase.meal_create import MealCreate
from src.app.controllers.meal_create_controller import MealCreateController

def meal_create_presenter():
    repository = MealRepositoryDB()
    use_case = MealCreate(repository)
    controller = MealCreateController(use_case)

    return controller.handle
