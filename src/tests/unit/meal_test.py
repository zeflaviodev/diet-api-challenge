from datetime import datetime
from src.domain.entity.meal import Meal

def test_meal():
    name = 'Nome teste'
    description = 'Descrição teste'
    meal_at = datetime.strptime('2023-01-01', '%Y-%m-%d')

    try:
        meal = Meal(
            name=name,
            description=description,
            meal_at=meal_at
        )
    except Exception as e:
        assert False, f'Erro ao validar o objeto: {e}'

    assert isinstance(meal, Meal)
    assert meal.name == name
    assert meal.description == description
    assert meal.meal_at == meal_at
    assert meal.in_diet


def test_meal_without_name():
    description = 'Descrição teste'
    meal_at = datetime.strptime('2023-01-01', '%Y-%m-%d')

    try:
        Meal(
            description=description,
            meal_at=meal_at
        )
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'

def test_meal_without_description():
    name = 'Nome teste'
    meal_at = datetime.strptime('2023-01-01', '%Y-%m-%d')

    try:
        Meal(
            name=name,
            meal_at=meal_at
        )
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'

def test_meal_without_meal_at():
    name = 'Nome teste'
    description = 'Descrição teste'

    try:
        Meal(
            name=name,
            description=description
        )
    except Exception as e:
        assert True
        assert str(e) == 'Todos os campos obrigatórios devem enviados!'

def test_meal_not_datetime_meat_at():
    name = 'Nome teste'
    description = 'Descrição teste'
    meal_at = '2023-01-01'

    try:
        Meal(
            name=name,
            description=description,
            meal_at=meal_at
        )
    except Exception as e:
        assert True
        assert str(e) == 'A data e horario da refeição deve ser do tipo datetime!'
