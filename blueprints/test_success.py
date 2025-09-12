from flask import Blueprint, request, jsonify
from extensions import db
from models.base import TestSuccess

home_bp = Blueprint('home',__name__)
test_success_bp = Blueprint("test_success", __name__, url_prefix="/test-success")

@test_success_bp.route('/home')
def printer():
    print('Print Success Route')
    return 'Hello world'

@home_bp.route('/')
def home():
    print('Home Page')
    return 'Home'