#pylint:disable=broad-exception-raised
from src.modules.shares.http.http_response import HttpResponse
from src.modules.shares.http.http_request import HttpRequest
from src.modules.meal.domain.meal_create import MealCreate
from src.modules.meal.use_case.create.meal_create_dto import InputMealCreateDto

class MealCreateController:

    def __init__(self, meal_create_use_case: MealCreate) -> None:
        self.__use_case = meal_create_use_case

    def handle(self, request: HttpRequest) -> HttpResponse:

        input_meal_create_dto = InputMealCreateDto(
            name=request.body["name"],
            description=request.body["description"],
            meal_at=request.body["meal_at"],
            in_diet=request.body["in_diet"]
        )

        response = self.__use_case.create_meal(input_meal_create_dto)

        return HttpResponse(
            status_code=201,
            body={
                "message": "Receita criada com sucesso!",
                "meal" : response
            }
        )
