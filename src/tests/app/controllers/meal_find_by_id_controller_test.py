from src.app.usecase.meal_find_by_id import MealFindById
from src.app.adapters.http_request import HttpRequest
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.controllers.meal_find_by_id_controller import MealFindByIdController


def test_meal_find_by_id_controller():

    http_request = HttpRequest(
        path_params={
            'id': 99
        }
    )

    repository = MealRepositoryMemory()

    use_case = MealFindById(repository)

    meal_find_by_id_controller = MealFindByIdController(use_case)

    try:
        response = meal_find_by_id_controller.handle(http_request)
    except Exception as e:
        assert False, f'Error: {e}'

    assert response
    assert response.body['data']
    assert response.body['data']['id'] == 99

def test_meal_find_by_id_controller_fail():

    http_request = HttpRequest(
        path_params={
            'id': 99
        }
    )

    repository = MealRepositoryMemory()

    use_case = MealFindById(repository)

    meal_find_by_id_controller = MealFindByIdController(use_case)

    try:
        meal_find_by_id_controller.handle(http_request)
    except Exception as e:
        assert True
        assert str(e) == 'Meal not found'
