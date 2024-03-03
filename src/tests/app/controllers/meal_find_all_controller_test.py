from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_find_all import MealFindAll
from src.app.controllers.meal_find_all_controller import MealFindAllController
from src.domain.entity.meal import Meal

def test_meal_find_all_controller():
    repository = MealRepositoryMemory()

    use_case = MealFindAll(repository)

    meal_find_all_controller = MealFindAllController(use_case)

    try:
        response = meal_find_all_controller.handle()
    except Exception as e:
        assert False, f'Error: {e}'

    assert response
    assert len(response.body['data']['meals']) == 6
    assert isinstance(response.body['data']['meals'].meals[0], Meal)
