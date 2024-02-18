from src.domain.meal.meal_entity import MealEntity

class MealRepositorySpy():
    def __init__(self):
        self.create_meal_params = {}
        self.find_meal_params = {}

    def create_meal(self, new_meal: MealEntity) -> None:
        self.create_meal_params['id'] = new_meal.id
        self.create_meal_params['name'] = new_meal.name
        self.create_meal_params['description'] = new_meal.description
        self.create_meal_params['meal_at'] = new_meal.meal_at
        self.create_meal_params['in_diet'] = new_meal.in_diet

    def find(self) -> None: pass
