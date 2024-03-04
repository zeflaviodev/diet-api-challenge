from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_delete import MealDelete
from src.app.usecase.meal_find_by_id import MealFindById
from src.app.controllers.meal_delete_controller import MealDeleteController

def test_meal_delete_controller():

    meal_id = 12

    repository = MealRepositoryMemory()

    meal_delete = MealDelete(repository)

    meal_delete_controller = MealDeleteController(meal_delete)

    try:
        meal_delete_controller.handle(meal_id)
    except Exception as e:
        assert False, f"Error: {e}"

    meal_find_by_id = MealFindById(repository)

    try:
        meal_find_by_id.execute(meal_id)
    except Exception as e:
        assert True
        assert str(e) == "Meal not found"

def test_meal_delete_controller_fail():

    meal_id = 12

    repository = MealRepositoryMemory()

    meal_delete = MealDelete(repository)

    meal_delete_controller = MealDeleteController(meal_delete)

    try:
        meal_delete_controller.handle(meal_id)
    except Exception as e:
        assert True
        assert str(e) == "Meal not found"
