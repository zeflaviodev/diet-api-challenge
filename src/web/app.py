from flask import Flask
from src.web.routes.meal_route import meal_router_bp

app = Flask(__name__)

app.register_blueprint(meal_router_bp)
