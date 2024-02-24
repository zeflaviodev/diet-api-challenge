from src.modules.meal.domain.meal_entity import MealEntity

class MealRepositorySpy:

    def __init__(self) -> None:
        self.create_meal_params = None
        self.find_by_id_params = {}

    def create_meal(self, meal: MealEntity) -> MealEntity:
        meal.id = 1
        self.create_meal_params = meal
        return meal

    def find_by_id(self, meal_id: int) -> MealEntity: pass
