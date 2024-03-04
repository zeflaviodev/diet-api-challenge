from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_find_by_id import MealFindById
from src.app.controllers.meal_find_by_id_controller import MealFindByIdController


def test_meal_find_by_id_controller():

    meal_id = 12

    repository = MealRepositoryMemory()

    use_case = MealFindById(repository)

    meal_find_by_id_controller = MealFindByIdController(use_case)

    try:
        response = meal_find_by_id_controller.handle(meal_id)
    except Exception as e:
        assert False, f'Error: {e}'

    assert response
    assert response.body['data']
    assert response.body['data'].id == 12

def test_meal_find_by_id_controller_fail():

    meal_id = 88

    repository = MealRepositoryMemory()

    use_case = MealFindById(repository)

    meal_find_by_id_controller = MealFindByIdController(use_case)

    try:
        meal_find_by_id_controller.handle(meal_id)
    except Exception as e:
        assert True
        assert str(e) == 'Meal not found'
