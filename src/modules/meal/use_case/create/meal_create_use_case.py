#pylint:disable=redefined-builtin,too-many-arguments
from src.modules.meal.domain.meal_entity import MealEntity
from src.modules.meal.domain.meal_create import MealCreate
from src.modules.meal.domain.meal_repository import MealRepository
from src.modules.meal.use_case.create.meal_create_dto import InputMealCreateDto, OutputealCreateDto

class MealCreateUseCase(MealCreate):

    def __init__(self, meal_repository: MealRepository ) -> None:
        self.meal_repository = meal_repository

    def create_meal(self, meal_dto: InputMealCreateDto) -> OutputealCreateDto:

        meal_entity = MealEntity(
            name = meal_dto.name,
            description = meal_dto.description,
            meal_at = meal_dto.meal_at,
            in_diet = meal_dto.in_diet
        )

        meal_entity.validate()

        meal = self.meal_repository.create(meal_entity)

        meal_output_dto = OutputealCreateDto(
            id = meal.id,
            name = meal.name,
            description = meal.description,
            meal_at = meal.meal_at,
            in_diet = meal.in_diet
        )

        return meal_output_dto
