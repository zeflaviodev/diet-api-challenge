#pylint:disable=redefined-builtin,line-too-long
from datetime import datetime
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal


class MealRepositoryMemory(MealRepositoryInterface):

    meals = [
        Meal(id=85, name="Nome Teste1", description="Descrição Teste1", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
        Meal(id=22, name="Nome Teste2", description="Descrição Teste2", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
        Meal(id=12, name="Nome Teste3", description="Descrição Teste3", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
        Meal(id=99, name="Nome Teste4", description="Descrição Teste4", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
        Meal(id=35, name="Nome Teste5", description="Descrição Teste4", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
        Meal(id=12, name="Nome Teste6", description="Descrição Teste5", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M"))
    ]

    @classmethod
    def create(cls, meal:Meal) -> Meal:
        meal.id = 99
        return meal

    def find_all(self) -> list[Meal]:
        return self.meals

    def find_by_id(self, id) -> Meal:
        for meal in self.meals:
            if meal.id == id:
                return meal
        return None

    def update(self, id: int, meal: Meal) -> Meal:

        index_meal = None
        for index, value in enumerate(self.meals):
            if value.id == id:
                index_meal = index
                break

        if not index_meal:
            return None

        self.meals[index_meal].name = meal.name
        self.meals[index_meal].description = meal.description
        self.meals[index_meal].meal_at = meal.meal_at
        self.meals[index_meal].in_diet = meal.in_diet
        return self.meals[index_meal]
