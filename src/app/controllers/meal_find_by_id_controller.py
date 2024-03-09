# pylint:disable=redefined-builtin
from src.app.adapters.http_request import HttpRequest
from src.app.adapters.http_response import HttpResponse
from src.domain.usecase.meal_find_by_id_interface import MealFindByIdInterface

class MealFindByIdController:
    def __init__(self, meal_find_by_id: MealFindByIdInterface):
        self.__use_case = meal_find_by_id

    def handle(self, request: HttpRequest) -> HttpResponse:

        response = self.__use_case.execute(request.path_params['id'])

        return HttpResponse(
            status_code=200,
            body={
                "data": response.__dict__
            }
        )
