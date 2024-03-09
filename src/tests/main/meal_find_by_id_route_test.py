from src.main.app import app

def test_meal_find_by_id_route():
    meal_id = 1

    try:
        response = app.test_client().get(f'/meals/{meal_id}')
    except Exception as e:
        assert False, f'Erro ao executar o teste: {e}'

    assert response.status_code == 200
    assert response.json['data']['id'] == meal_id


def test_meal_find_by_id_route_fail():
    meal_id = 123123123123123123

    try:
        app.test_client().get(f'/meals/{meal_id}')
    except Exception as e:
        assert True
        assert str(e) == 'Meal not found'
