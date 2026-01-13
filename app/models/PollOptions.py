from app import db


class PollOptions(db.Model):
    option_id: int
    poll_id: int
    option_text: str
    votes: int

    __tablename__ = 'poll_options'

    option_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.poll_id'), nullable=False)
    option_text = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, poll_id: int, option_text: str):
        self.poll_id = poll_id
        self.option_text = option_text
        self.votes = 0