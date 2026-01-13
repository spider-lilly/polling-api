from sqlalchemy import UniqueConstraint
from app import db
class votes(db.Model):
    vote_id: int
    user_id: str
    poll_id: int
    option: str
    __tablename__ = 'votes'
    vote_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(80), db.ForeignKey('users.user_id'), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.poll_id'), nullable=False)
    option = db.Column(db.String(200), nullable=False)
    __table_args__ = (UniqueConstraint('poll_id', 'user_id', name='unique_user_vote'),)