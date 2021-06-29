from flask import Blueprint, request, jsonify, make_response
from app import db
from .models.board import Board
from .models.card import Card
import os


# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("cards", __name__, url_prefix="/cards")

@card_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_card():
    request_body = request.ge.json()

    if "title" not in request_body:
        return jsonify(details="invalid data"), 400
    
    new_board = Board.from_json(request_body)

    db.session.add(new_board)
    db.session.commit()

    return new_board.to_json_goal(), 201