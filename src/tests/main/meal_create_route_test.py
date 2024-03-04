from src.main.app import app


def test_meal_create_route():

    request_json = {
        'name': 'teste',
        'description': 'teste',
        'meal_at': '2024-03-01 20:00',
        'in_diet': True
    }

    try:
        response = app.test_client().post('/meals', json=request_json)
    except Exception as e:
        assert False, f'Erro ao executar o teste: {e}'

    assert response.status_code == 200
    assert response.json['data']['meal']['name'] == request_json['name']
    assert response.json['data']['meal']['description'] == request_json['description']
    assert response.json['data']['meal']['in_diet'] == request_json['in_diet']
