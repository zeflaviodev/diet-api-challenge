from cerberus import Validator
from src.errors.types.unprocessable_entity_error import UnprocessableEntityError

class MealValidator:

    @classmethod
    def create_validator(cls, request: any):
        body_validator = Validator({
            'name': {'type': 'string', 'required': True, "empty": False},
            'description': {'type': 'string', 'required': True, "empty": False},
            'meal_at': {'type': 'datetime', 'required': True, "empty": False},
            'in_diet': {'type': 'boolean', 'required': True, "empty": False}
        })
        response = body_validator.validate(request.json)
        if response is False:
            raise UnprocessableEntityError(body_validator.errors)
