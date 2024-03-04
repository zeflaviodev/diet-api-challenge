# pylint:disable=redefined-builtin
from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_find_all_interface import MealFindAllInterface

class MealFindByIdController:
    def __init__(self, meal_create: MealFindAllInterface):
        self.__use_case = meal_create

    def handle(self, id: int) -> HttpResponse:

        response = self.__use_case.execute(id)

        return HttpResponse(
            status_code=200,
            body={
                "data": response
            }
        )
