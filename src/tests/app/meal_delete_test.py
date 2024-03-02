from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_delete import MealDelete
from src.app.usecase.meal_find_by_id import MealFindById


def test_meal_delete():

    repository = MealRepositoryMemory()

    meal_delete = MealDelete(repository)

    try:
        meal_delete.execute(12)
    except Exception as e:
        assert False, f"Error: {e}"

    meal_find_by_id = MealFindById(repository)

    try:
        meal_find_by_id.execute(12)
    except Exception as e:
        assert True
        assert str(e) == "Meal not found"

def test_meal_delete_fail_not_found():

    meal_id = 15000

    repository = MealRepositoryMemory()

    meal_delete = MealDelete(repository)

    try:
        meal_delete.execute(meal_id)
    except Exception as e:
        assert True
        assert str(e) == "Meal not found"
