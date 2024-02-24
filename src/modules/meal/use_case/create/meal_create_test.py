#pylint:disable=redefined-builtin
from datetime import datetime
from src.modules.meal.infrastructure.tests.meal_repository_spy import MealRepositorySpy
from src.modules.meal.use_case.create.meal_create_use_case import MealCreateUseCase
from src.modules.meal.use_case.create.meal_create_dto import InputMealCreateDto

def test_meal_create():
    name='test'
    description='test'
    meal_at=datetime.now()
    in_diet=False

    repository = MealRepositorySpy()

    meal_create = MealCreateUseCase(repository)

    meal_dto = InputMealCreateDto(
        name=name,
        description=description,
        meal_at=meal_at,
        in_diet=in_diet
    )

    response = meal_create.create_meal(meal_dto)

    assert repository.create_meal_params.name == name
    assert repository.create_meal_params.description == description
    assert repository.create_meal_params.meal_at == meal_at
    assert repository.create_meal_params.in_diet == in_diet

    assert response.name == name
    assert response.description == description

def test_meal_createfail():
    name=''
    description='test'
    meal_at=datetime.now()
    in_diet=False

    repository = MealRepositorySpy()

    meal_create = MealCreateUseCase(repository)

    meal_dto = InputMealCreateDto(
        name=name,
        description=description,
        meal_at=meal_at,
        in_diet=in_diet
    )

    try:
        meal_create.create_meal(meal_dto)
        assert False, 'Não está validando os campos corretamente'
    except Exception as error:
        assert str(error) == 'Todos os campos obrigatórios devem enviados!'
