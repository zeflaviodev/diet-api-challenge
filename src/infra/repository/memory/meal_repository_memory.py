from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal


class MealRepositoryMemory(MealRepositoryInterface):

    @classmethod
    def create(cls, meal:Meal) -> Meal:
        meal.id = 99
        return meal
