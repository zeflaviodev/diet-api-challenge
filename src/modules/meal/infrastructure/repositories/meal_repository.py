from src.modules.meal.domain.meal_repository import MealRepository as MealRepositoryInterface
from src.database.settings.connection import DBConnectionHandler
from src.modules.meal.domain.meal_entity import MealEntity
from src.modules.meal.infrastructure.models.meal_model import MealModel

class MealRepository(MealRepositoryInterface):

    @classmethod
    def create(cls, meal: MealEntity) -> MealEntity:

        meal_model = MealModel(
            name = meal.name,
            description = meal.description,
            meal_at = meal.meal_at,
            in_diet = meal.in_diet
        )

        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(meal_model)
                db_connection.session.commit()
                meal_response = MealEntity(
                    id=meal_model.id,
                    name=meal_model.name,
                    description=meal_model.description,
                    meal_at=meal_model.meal_at,
                    in_diet=meal_model.in_diet
                )
                return meal_response
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, meal_id: int) -> MealModel: pass
