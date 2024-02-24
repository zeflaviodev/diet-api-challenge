from src.modules.meal.domain.meal_repository import MealRepository as MealRepositoryInterface
from src.database.settings.connection import DBConnectionHandler
from src.modules.meal.domain.meal_entity import MealEntity

class MealRepository(MealRepositoryInterface):

    @classmethod
    def create(cls, meal: MealEntity) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(meal)
                db_connection.session.commit()
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, meal_id: int) -> MealEntity: pass
