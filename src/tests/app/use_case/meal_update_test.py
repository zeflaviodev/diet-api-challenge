from datetime import datetime
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.app.usecase.meal_find_by_id import MealFindById
from src.app.usecase.meal_update import MealUpdate
from src.domain.usecase.meal_update_interface import InputMealUpdate

def test_meal_update():
    name = 'Teste'
    description = 'Teste'
    meal_at = datetime.strptime('2024-03-01 20:00', '%Y-%m-%d %H:%M')
    in_diet = True

    repository = MealRepositoryMemory()

    meal_update = MealUpdate(repository)

    input_meal_update = InputMealUpdate(
        name=name,
        description=description,
        meal_at=meal_at,
        in_diet=in_diet,
    )

    try:
        meal_update = meal_update.execute(
            id=12,
            input_meal_update=input_meal_update
        )
    except Exception as e:
        assert False, f'Error: {e}'

    meal_find_by_id = MealFindById(repository)

    meal = meal_find_by_id.execute(id=12)

    assert meal_update.id == 12
    assert meal.name == input_meal_update.name
    assert meal.description == input_meal_update.description
    assert meal.meal_at == input_meal_update.meal_at
    assert meal.in_diet == input_meal_update.in_diet


def test_meal_update_fail():
    description = 'Teste'
    meal_at = datetime.strptime('2024-03-01 20:00', '%Y-%m-%d %H:%M')
    in_diet = True

    repository = MealRepositoryMemory()

    meal_update = MealUpdate(repository)

    input_meal_update = InputMealUpdate(
        description=description,
        meal_at=meal_at,
        in_diet=in_diet,
    )

    try:
        meal_update = meal_update.execute(
            id=12,
            input_meal_update=input_meal_update
        )
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'
