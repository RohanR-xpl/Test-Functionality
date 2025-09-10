from flask import Blueprint, request, jsonify
from extensions import db
from models.base import TestSuccess

test_success_bp = Blueprint("test_success", __name__, url_prefix="/test-success")

@test_success_bp.route('/home')
def printer():
    print('Print Success Route')
    return 'Hello world'