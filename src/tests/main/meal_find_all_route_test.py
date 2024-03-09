from src.main.app import app


def test_meal_find_all_route():

    try:
        response = app.test_client().get('/meals')
    except Exception as e:
        assert False, f'Erro ao executar o teste: {e}'

    assert response.status_code == 200
    # assert response.json['data']['meals']['name'] == request_json['name']
    # assert response.json['data']['meal']['description'] == request_json['description']
    # assert response.json['data']['meal']['in_diet'] == request_json['in_diet']
