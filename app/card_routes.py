from flask import Blueprint, request, jsonify, make_response
from app import db
from .models.board import Board
from .models.card import Card
import os


# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("cards", __name__, url_prefix="/cards")

@card_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_card():
    request_body = request.get.json()

    if "message" not in request_body:
        return jsonify(details="invalid data"), 400
    
    new_card = card.from_json(request_body)

    db.session.add(new_card)
    db.session.commit()

    return new_card.to_json_card(), 201

@card_bp.route("", methods=["DELETE"], strict_slashes=False)
def delete_a_card():
    pass

#update a card
# @card_bp.route("", methods=["PUT"], strict_slashes=False)
# def like_a_card():
#     pass


@card_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_cards():
    pass

