from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_find_by_id import MealFindById
from src.domain.entity.meal import Meal


def test_meal_find_by_id():

    repository = MealRepositoryMemory()

    meal_find_by_id = MealFindById(repository)

    try:
        meal = meal_find_by_id.execute(99)
    except Exception as e:
        assert False, f"Error: {e}"

    assert isinstance(meal, Meal)
    assert meal.id == 99
    assert meal.name == "Nome Teste4"
    assert meal.description == "Descrição Teste4"

def test_meal_find_by_id_not_found():
    repository = MealRepositoryMemory()

    meal_find_by_id = MealFindById(repository)

    try:
        meal_find_by_id.execute(99)
    except Exception as e:
        assert True
        assert str(e) == "Meal not found"
