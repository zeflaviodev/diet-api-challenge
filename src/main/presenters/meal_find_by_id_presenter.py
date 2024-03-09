# pylint:disable=redefined-builtin
from src.infra.repository.db.meal_repository_db import MealRepositoryDB
from src.app.usecase.meal_find_by_id import MealFindById
from src.app.controllers.meal_find_by_id_controller import MealFindByIdController

def meal_find_by_id_presenter():
    repository = MealRepositoryDB()
    use_case = MealFindById(repository)
    controller = MealFindByIdController(use_case)

    return controller.handle
