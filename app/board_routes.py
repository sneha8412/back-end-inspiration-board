from flask import Blueprint, request, jsonify, make_response
from app import db
from .models.board import Board
from .models.card import Card
import os


# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_board():
    request_body = request.ge.json()

    if "title" not in request_body:
        return jsonify(details="invalid data"), 400
    
    new_board = Board.from_json(request_body)

    db.session.add(new_board)
    db.session.commit()

    return new_board.to_json_goal(), 201


@board_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_boards():
    
    board_list = Board.query.all()
    
    Board_response = [] 
    for board in board_list:
        board_response.append(board.to_json_board_no_key())
    
    return jsonify(board_response), 200


@board_bp.route("<board_id>", methods=["GET"], strict_slashes=False)
def get_one_board(board_id):
    
    if not helper.is_int(board_id):
        return {
            "message": "id must be an integer",
            "success": False
        },400
        
    board = Board.query.get(board_id)
    
    if board == None:
        return Response("",status=404)
    
    if board:
        return board.to_json_board(), 200


@gboard_bp.route("<board_id>", methods=["DELETE"], strict_slashes=False)
def delete_board(board_id):

    board = Board.query.get(board_id)

    if board == None:
        return Response("", status=404)

    if board:
        db.session.delete(board)
        db.session.commit()
        
        board_details = f"Board {board.board_id} \"{board.title}\" successfully deleted"
        
        return jsonify(details=board_details
                         ),200


#list posts (<board_id>)