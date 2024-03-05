from src.infra.repository.db.meal_repository_db import MealRepositoryDB
from src.app.usecase.meal_find_all import MealFindAll
from src.app.controllers.meal_find_all_controller import MealFindAllController

def meal_find_all_presenter():
    repository = MealRepositoryDB()
    use_case = MealFindAll(repository)
    controller = MealFindAllController(use_case)

    return controller.handle
