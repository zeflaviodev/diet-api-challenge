from datetime import datetime
from src.infra.repository.memory.meal_repository_memory import MealRepositoryMemory
from src.domain.usecase.meal_create_interface import InputMealCreate
from src.app.usecase.meal_create import MealCreate

def test_meal_create():
    name="test"
    description="test"
    meal_at=datetime.strptime('2024-02-29 21:30', "%Y-%m-%d %H:%M")

    repository = MealRepositoryMemory()
    meal_create = MealCreate(repository)

    input_meal_create = InputMealCreate(
        name=name,
        description=description,
        meal_at=meal_at,
    )

    try:
        new_meal = meal_create.execute(input_meal_create)
    except Exception as e:
        assert False, f'Erro ao tentar criar: {e}'

    assert new_meal.id is not None
    assert new_meal.name == name
    assert new_meal.description == description
    assert new_meal.meal_at == meal_at
    assert new_meal.in_diet

def test_meal_create_fail():
    description="test"
    meal_at=datetime.strptime('2024-02-29 21:30', "%Y-%m-%d %H:%M")

    repository = MealRepositoryMemory()
    meal_create = MealCreate(repository)

    input_meal_create = InputMealCreate(
        description=description,
        meal_at=meal_at,
    )

    try:
        meal_create.execute(input_meal_create)
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'
