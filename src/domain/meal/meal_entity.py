#pylint: disable=too-many-arguments, redefined-builtin
from datetime import datetime
from src.errors.types.bad_request_error import BadRequestError

class MealEntity:
    def __init__(self, id: int, name: str, description: str, meal_at: datetime, in_diet: bool) :
        self.id = id
        self.name = name
        self.description = description
        self.meal_at = meal_at
        self.in_diet = in_diet

    def validate(self) -> bool:
        if not self.name or not self.description or not self.meal_at or not self.in_diet:
            raise BadRequestError('Todos os campos obrigatórios devem enviados!')

        if not isinstance(self.meal_at, datetime):
            raise BadRequestError('A data e horario da refeição deve ser do tipo datetime!')

        return True
