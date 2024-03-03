# pylint:disable=line-too-long
from datetime import datetime
from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.app.controllers.meal_create_controller import MealCreateController
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_create import MealCreate

def test_meal_create_controller():
    http_request = HttpRequest(
        body = {
            "name": "test",
            "description": "test",
            "meal_at": datetime.strptime('2024-02-29', '%Y-%m-%d'),
            "in_diet": True
        }
    )

    repository = MealRepositoryMemory()

    use_case = MealCreate(repository)

    meal_create_controller = MealCreateController(use_case)

    try:
        response = meal_create_controller.handle(http_request)
    except Exception as e:
        assert False, f'Error: {e}'

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
    assert response.body['data']['meal'].name == http_request.body['name']
    assert response.body['data']['meal'].description == http_request.body['description']
    assert response.body['data']['meal'].meal_at == http_request.body['meal_at'].strftime('%Y-%m-%d %H:%M')
    assert response.body['data']['meal'].in_diet == http_request.body['in_diet']

def test_meal_create_controller_fail():
    http_request = HttpRequest(
        body = {
            # "name": "test",
            "description": "test",
            "meal_at": datetime.strptime('2024-02-29', '%Y-%m-%d'),
            "in_diet": True
        }
    )

    repository = MealRepositoryMemory()

    use_case = MealCreate(repository)

    meal_create_controller = MealCreateController(use_case)

    try:
        meal_create_controller.handle(http_request)
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'
