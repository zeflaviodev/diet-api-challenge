# pylint: disable=redefined-builtin,broad-exception-raised
from src.domain.usecase.meal_delete_interface import MealDeleteInterface
from src.domain.repository.meal_repository_interface import MealRepositoryInterface


class MealDelete(MealDeleteInterface):

    def __init__(self, respository: MealRepositoryInterface):
        self.respository = respository

    def execute(self, id: int) -> None:

        meal = self.respository.find_by_id(id)
        if not meal:
            raise Exception('Meal not found')

        try:
            self.respository.delete(meal.id)
        except Exception as error:
            raise f'Error to delete meal: {error}'
