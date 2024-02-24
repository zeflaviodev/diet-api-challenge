#pylint:disable=broad-exception-raised
from datetime import datetime
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
            meal_at= datetime.strptime(request.body["meal_at"], "%Y-%m-%d"),
            in_diet=request.body["in_diet"]
        )

        meal = self.__use_case.create_meal(input_meal_create_dto)

        return HttpResponse(
            status_code=201,
            body={
                "message": "Receita criada com sucesso!",
                "data": {
                    "meal" : {
                        "id": meal.id,
                        "name": meal.name,
                        "description": meal.description,
                        "meal_at": meal.meal_at,
                        "in_diet": meal.in_diet
                    }
                }
            }
        )
