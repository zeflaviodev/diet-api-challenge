from sqlalchemy import String, Column, Integer, DateTime, Boolean
from src.infra.db.settings.base import Base


class MealModel(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    meal_at = Column(DateTime, nullable=False)
    in_diet = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Meal [id={self.id}, name={self.name}]>"
