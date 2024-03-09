#pylint:disable=line-too-long,redefined-builtin,unused-argument
from flask import Blueprint, request, jsonify
from src.app.adapters.request_adapter import request_adapter
from src.main.presenters.meal_create_presenter import meal_create_presenter
from src.main.presenters.meal_find_all_presenter import meal_find_all_presenter
from src.main.presenters.meal_find_by_id_presenter import meal_find_by_id_presenter

meal_router_bp = Blueprint('meal_routers', __name__)

@meal_router_bp.route('/meals', methods=['POST'])
def create_meal():
    http_response = None
    try:
        http_response = request_adapter(request, meal_create_presenter())
    except Exception as exception:
        raise exception
    return jsonify(http_response.body), http_response.status_code

@meal_router_bp.route('/meals', methods=['GET'])
def find_all_meal():
    http_response = None
    try:
        http_response = request_adapter(request, meal_find_all_presenter())
    except Exception as exception:
        raise exception
    return jsonify(http_response.body), http_response.status_code

@meal_router_bp.route('/meals/<int:id>', methods=['GET'])
def find_by_id(id: int):
    http_response = None
    try:
        http_response = request_adapter(request, meal_find_by_id_presenter())
    except Exception as exception:
        raise exception
    return jsonify(http_response.body), http_response.status_code
