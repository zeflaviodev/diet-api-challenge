from flask import Flask
from src.main.routes.meal_router import meal_router_bp

app = Flask(__name__)

app.register_blueprint(meal_router_bp)
