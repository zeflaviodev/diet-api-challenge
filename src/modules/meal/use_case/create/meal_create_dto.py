#pylint:disable=redefined-builtin,too-many-arguments
from datetime import datetime
from dataclasses import dataclass

class InputMealCreateDto() :
    def __init__(self, name: str, description: str, meal_at: datetime, in_diet: bool):
        self.name = name
        self.description = description
        self.meal_at = meal_at
        self.in_diet = in_diet

# class OutputealCreateDto() :
#     def __init__(self, id: int, name: str, description: str, meal_at: datetime, in_diet: bool):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.meal_at = meal_at
#         self.in_diet = in_diet
@dataclass
class OutputealCreateDto() :
    id: int
    name: str
    description: str
    meal_at: str|datetime
    in_diet: bool

    def __json__(self):
        # Personalize a serialização para JSON
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "meal_at": self.meal_at.strftime("%Y-%m-%d"),
            "in_diet": self.in_diet
        }
