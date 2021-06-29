from app import db
from flask import current_app

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)

    def to_json_board(self):

        return{
            "board":
            {
                "id" :self.board_id,
                "title": self.title      
            }
        }
    
    def to_json_board_no_key(self):
        return {
            "id" : self.board_id,
            "title": self.title
        }

    @staticmethod
    def from_json(board_json):
        return Board(title=board_json["title"])