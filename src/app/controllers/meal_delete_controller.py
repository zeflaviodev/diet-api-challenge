from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_delete_interface import MealDeleteInterface

class MealDeleteController:

    def __init__(self, meal_delete: MealDeleteInterface):
        self.__use_case = meal_delete

    def handle(self, meal_id: int) -> HttpResponse:

        self.__use_case.execute(meal_id)

        return HttpResponse(
            status_code=200,
            body=None
        )
