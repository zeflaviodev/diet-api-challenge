#pylint:disable=line-too-long
from datetime import datetime
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal


class MealRepositoryMemory(MealRepositoryInterface):

    @classmethod
    def create(cls, meal:Meal) -> Meal:
        meal.id = 99
        return meal

    @classmethod
    def find_all(cls) -> list[Meal]:
        return [
            Meal(id=85, name="Nome Teste1", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
            Meal(id=22, name="Nome Teste2", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
            Meal(id=12, name="Nome Teste3", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
            Meal(id=99, name="Nome Teste4", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
            Meal(id=35, name="Nome Teste5", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M")),
            Meal(id=12, name="Nome Teste6", description="Descrição Teste", meal_at=datetime.strptime("2024-02-29 20:00", "%Y-%m-%d %H:%M"))
        ]
