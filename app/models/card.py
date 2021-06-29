from app import db
from flask import current_app

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def to_json_card(self):

        return{
            "board":
            {
                "id" :self.card_id,
                "message": self.message     
            }
        }
    
    def to_json_no_key(self):
        return {
            "id" : self.card_id,
            "message": self.message
        }

    @staticmethod
    def from_json(card_json):
        return Card(message=card_json["message"])