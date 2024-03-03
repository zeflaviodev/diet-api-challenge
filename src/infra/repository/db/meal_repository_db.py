# pylint:disable=redefined-builtin
from src.domain.entity.meal import Meal
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
# from src.infra.db.settings.connection import DBConnectionHandler

class MealRepositoryDB(MealRepositoryInterface):

    def create(self, meal: Meal) -> Meal: pass
        # meal_model = MealModel(
        #     name = meal.name,
        #     description = meal.description,
        #     meal_at = meal.meal_at,
        #     in_diet = meal.in_diet
        # )

        # with DBConnectionHandler() as db_connection:
        #     try:
        #         db_connection.session.add(meal_model)
        #         db_connection.session.commit()
        #         meal_response = MealEntity(
        #             id=meal_model.id,
        #             name=meal_model.name,
        #             description=meal_model.description,
        #             meal_at=meal_model.meal_at,
        #             in_diet=meal_model.in_diet
        #         )
        #         return meal_response
        #     except Exception as exception:
        #         db_connection.session.rollback()
        #         raise exception

    def find_all(self) -> list[Meal]: pass
        # with DBConnectionHandler() as db_connection:
        #     try:
        #         meal_models = db_connection.session.query(MealModel).all()
        #         meals = [
        #             MealEntity(
        #                 id=meal_model.id,
        #                 name=meal_model.name,
        #                 description=meal_model.description,
        #                 meal_at=meal_model.meal_at,
        #                 in_diet=meal_model.in_diet
        #             )
        #             for meal_model in meal_models
        #         ]
        #         return meals
        #     except Exception as exception:
        #         raise exception

    def find_by_id(self, id: int) -> Meal: pass

    def update(self, id: int, meal: Meal) -> Meal: pass

    def delete(self, id: int) -> None: pass
