from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.usecase.meal_find_all_interface import MealFindAllInterface, OutputMealFindAll

class MealFindAll(MealFindAllInterface):

    def __init__(self, repository: MealRepositoryInterface) -> None:
        self.repository = repository


    def execute(self) -> OutputMealFindAll:

        meals = self.repository.find_all()

        return OutputMealFindAll(meals=meals)
