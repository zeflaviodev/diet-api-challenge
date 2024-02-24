from datetime import datetime

class HttpCreateRequestMock():
    def __init__(self):
        self.request = {
            "data": 'data',
            "json": {
                "name": "name",
                "description": "description",
                "meal_at": datetime.now()
            },
        }

# def test_meal_controller_create():
#     http_request_mock = HttpCreateRequestMock()
