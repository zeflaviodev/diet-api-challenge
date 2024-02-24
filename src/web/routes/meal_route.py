from flask import Blueprint, request, jsonify
# from src.adapters.request_adapter import request_adapter
# from src.application.meal.meal_controller import MealController
# from src.application.meal.meal_service import MealService
# from src.errors.error_handler import handle_errors
from src.modules.meal.infrastructure.controllers.meal_controller import MealController
# from src.infrastructure.database.repositories.meal_repository import MealRepository

meal_router_bp = Blueprint('meal_routers', __name__)

@meal_router_bp.route('/meals', methods=['POST'])
def create_meal():
    http_response = None
    try:
        meal_controller = MealController()
        http_response = meal_controller.create(request)
    except Exception as exception:
        raise exception
    return jsonify(http_response), 201
