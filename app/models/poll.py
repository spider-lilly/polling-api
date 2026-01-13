
from app import db
from datetime import datetime, timedelta

class poll(db.Model):
    poll_id: int
    question: str
    options: list

    __tablename__ = 'poll'
    poll_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.PickleType, nullable=False)
    closes = db.Column(db.DateTime, nullable=False)
    def __init__(self, question: str, options: list, closes: datetime):
        self.question = question
        self.options = options
        self.closes = closes
    def is_closed(self) -> bool:
        return datetime.now() >= self.closes