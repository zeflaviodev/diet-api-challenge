from src.app.adapters.http_request import HttpRequest
from src.app.usecase.meal_find_all import MealFindAll
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.controllers.meal_find_all_controller import MealFindAllController


def test_meal_find_all_controller():

    http_request = HttpRequest()

    repository = MealRepositoryMemory()

    use_case = MealFindAll(repository)

    meal_find_all_controller = MealFindAllController(use_case)

    try:
        response = meal_find_all_controller.handle(http_request)
    except Exception as e:
        assert False, f'Error: {e}'

    assert len(response.body['data']['meals']) == 4
