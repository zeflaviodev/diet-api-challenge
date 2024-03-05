from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_find_all_interface import MealFindAllInterface

class MealFindAllController:
    def __init__(self, meal_create: MealFindAllInterface):
        self.__use_case = meal_create

    # pylint: disable=unused-argument
    def handle(self, request: HttpRequest) -> HttpResponse:

        response = self.__use_case.execute()

        meals = [meal.__dict__ for meal in response.meals]

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "meals": meals
                }
            }
        )
