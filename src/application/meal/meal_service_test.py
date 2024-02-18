from datetime import datetime
from src.domain.meal.meal_entity import MealEntity
from src.infrastructure.tests.repositories.meal_repository_spy import MealRepositorySpy
from .meal_service import MealService

def test_create_meal() :
    new_meal = MealEntity(
        id=2,
        name="Almoco",
        description="Almoco comendo arroz",
        meal_at= datetime(2024, 2, 18, 12, 15),
        in_diet=True,
    )

    repository = MealRepositorySpy()
    meal_service = MealService(repository)

    response = meal_service.create(new_meal)

    assert repository.create_meal_params['id'] == new_meal.id
    assert repository.create_meal_params['name'] == new_meal.name
    assert repository.create_meal_params['description'] == new_meal.description
    assert repository.create_meal_params['meal_at'] == new_meal.meal_at
    assert repository.create_meal_params['in_diet'] == new_meal.in_diet

    assert response['meal']

def test_create_meal_fail_invalid_data() :
    new_meal = MealEntity(
        id=2,
        name="Almoco",
        description="",
        meal_at= datetime(2024, 2, 18, 12, 15),
        in_diet=True,
    )

    repository = MealRepositorySpy()
    meal_service = MealService(repository)

    try:
        meal_service.create(new_meal)
        assert False
    except Exception as e:
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'

def test_create_meal_fail_type_datetime() :
    new_meal = MealEntity(
        id=2,
        name="Almoco",
        description="Descricao teste",
        meal_at= '2024-02-18',
        in_diet=True,
    )

    repository = MealRepositorySpy()
    meal_service = MealService(repository)

    try:
        meal_service.create(new_meal)
        assert False
    except Exception as e:
        assert str(e) == 'A data e horario da refeição deve ser do tipo datetime!'
