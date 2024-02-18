from src.domain.meal.meal_respository_interface import MealRepositoryInterface
from src.domain.meal.meal_service_interface import MealServiceInterface
from src.domain.meal.meal_entity import MealEntity

class MealService(MealServiceInterface):
    def __init__(self, meal_repository: MealRepositoryInterface) -> None:
        self.meal_repository = meal_repository

    def find(self) -> MealEntity: pass

    def create(self, new_meal: MealEntity) -> None:

        new_meal.validate()

        self.meal_repository.create_meal(new_meal)

        return {
            "meal": {
                "id": new_meal.id,
                "name": new_meal.name,
                "description": new_meal.description,
                "meal_at": new_meal.meal_at,
                "in_diet": new_meal.in_diet
            }
        }
