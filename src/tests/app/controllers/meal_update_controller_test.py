from datetime import datetime
from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_update import MealUpdate
from src.app.controllers.meal_update_controller import MealUpdateController


def test_meal_update_controller():

    http_request = HttpRequest(
        body = {
            "id": 12,
            "name": "test",
            "description": "test",
            "meal_at": datetime.strptime('2024-02-29', '%Y-%m-%d'),
            "in_diet": True
        }
    )

    meal_id = http_request.body.get('id')

    repository = MealRepositoryMemory()

    meal_update = MealUpdate(repository)

    meal_update_controller = MealUpdateController(meal_update)

    try:
        response = meal_update_controller.handle(meal_id, http_request)
    except Exception as e:
        assert False,  f'Error: {e}'

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
    assert response.body['data']['meal'].id == meal_id
    assert response.body['data']['meal'].name == http_request.body.get('name')
    assert response.body['data']['meal'].description == http_request.body.get('description')

def test_meal_update_controller_fail():

    http_request = HttpRequest(
        body = {
            "id": 12,
            "description": "test",
            "meal_at": datetime.strptime('2024-02-29', '%Y-%m-%d'),
            "in_diet": True
        }
    )

    meal_id = http_request.body.get('id')

    repository = MealRepositoryMemory()

    meal_update = MealUpdate(repository)

    meal_update_controller = MealUpdateController(meal_update)

    try:
        meal_update_controller.handle(meal_id, http_request)
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'
