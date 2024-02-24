#pylint:disable=line-too-long
from flask import Blueprint, request, jsonify
from src.modules.meal.infrastructure.presenters.create.meal_create_presenter import meal_create_presenter
from src.web.adapters.request_adapater import request_adapter

meal_router_bp = Blueprint('meal_routers', __name__)

@meal_router_bp.route('/meals', methods=['POST'])
def create_meal():
    http_response = None
    try:
        http_response = request_adapter(request, meal_create_presenter())
    except Exception as exception:
        raise exception
    return jsonify(http_response.body), http_response.status_code
