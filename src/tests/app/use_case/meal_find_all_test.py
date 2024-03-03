from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_find_all import MealFindAll
from src.domain.usecase.meal_find_all_interface import OutputMealFindAll
from src.domain.entity.meal import Meal

def test_meal_find_all():

    repository = MealRepositoryMemory()
    meal_find_all = MealFindAll(repository)

    try:
        response = meal_find_all.execute()
    except Exception as e:
        assert False, f"Erro ao buscar as receitas: {e}"

    assert response
    assert len(response.meals) == 6
    assert isinstance(response, OutputMealFindAll)
    assert isinstance(response.meals[0], Meal)
