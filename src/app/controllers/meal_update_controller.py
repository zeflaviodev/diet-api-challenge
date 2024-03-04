from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_update_interface import MealUpdateInterface, InputMealUpdate

class MealUpdateController:

    def __init__(self, meal_update: MealUpdateInterface):
        self.__use_case = meal_update

    def handle(self, meal_id: int,  request: HttpRequest) -> HttpResponse:
        body = request.body

        input_meal_update = InputMealUpdate(
            name=body.get('name'),
            description=body.get('description'),
            meal_at=body.get('meal_at'),
            in_diet=body.get('in_diet')
        )

        response = self.__use_case.execute(meal_id, input_meal_update)

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "meal": response
                }
            }
        )
