from datetime import datetime
from src.errors.types.bad_request_error import BadRequestError

class Meal:
    def __init__(self,
        id: int = None,
        name: str = '',
        description: str = '',
        meal_at: datetime = None,
        in_diet: bool = True
    ) :
        #pylint: disable=too-many-arguments, redefined-builtin
        self.id = id
        self.name = name
        self.description = description
        self.meal_at = meal_at
        self.in_diet = in_diet

        self.__validate()

    def __validate(self) -> None:
        if not self.name or not self.description or not self.meal_at:
            raise BadRequestError('Todos os campos obrigatórios devem enviados!')

        if not isinstance(self.meal_at, datetime):
            raise BadRequestError('A data e horario da refeição deve ser do tipo datetime!')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'meal_at': self.meal_at,
            'in_diet': self.in_diet
        }
