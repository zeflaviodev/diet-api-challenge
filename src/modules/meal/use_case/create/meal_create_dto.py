#pylint:disable=redefined-builtin,too-many-arguments
from datetime import datetime

class InputMealCreateDto() :
    def __init__(self, name: str, description: str, meal_at: datetime, in_diet: bool):
        self.name = name
        self.description = description
        self.meal_at = meal_at
        self.in_diet = in_diet

class OutputealCreateDto() :
    def __init__(self, id: int, name: str, description: str, meal_at: datetime, in_diet: bool):
        self.id = id
        self.name = name
        self.description = description
        self.meal_at = meal_at
        self.in_diet = in_diet
