from flask import Blueprint, make_response, jsonify

health: Blueprint = Blueprint('health', __name__)


@health.route('/health', methods=['GET'])
def get_service_health():
    return make_response(jsonify({"health": "Service is up"}), 200)
