from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_create_interface import MealCreateInterface
from src.domain.usecase.meal_create_interface import InputMealCreate

class MealCreateController:

    def __init__(self, meal_create: MealCreateInterface):
        self.__use_case = meal_create

    def handle(self, request: HttpRequest) -> HttpResponse:
        body = request.body

        input_meal_create = InputMealCreate(
            name=body.get('name'),
            description=body.get('description'),
            meal_at=body.get('meal_at'),
            in_diet=body.get('in_diet')
        )

        response = self.__use_case.execute(input_meal_create)

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "meal": response
                }
            }
        )
