#pylint:disable=redefined-builtin,broad-exception-raised
from src.domain.usecase.meal_find_by_id_interface import MealFindByIdInterface
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal


class MealFindById(MealFindByIdInterface):

    def __init__(self, respository: MealRepositoryInterface):
        self.repository = respository

    def execute(self, id: int) -> Meal:
        meal = self.repository.find_by_id(id)

        if meal is None:
            raise Exception('Meal not found')

        return Meal(
            id=meal.id,
            name=meal.name,
            description=meal.description,
            meal_at=meal.meal_at,
            in_diet=meal.in_diet
        )
