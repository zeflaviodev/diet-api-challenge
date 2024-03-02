# pylint:disable=redefined-builtin
from abc import ABC, abstractmethod
from src.domain.repository.meal_repository_interface import MealRepositoryInterface
from src.domain.entity.meal import Meal


class MealFindByIdInterface(ABC):

    def __init__(self, repository: MealRepositoryInterface) -> None: pass

    @abstractmethod
    def execute(self, id: int) -> Meal: pass
