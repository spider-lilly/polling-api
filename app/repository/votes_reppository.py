from app import db
from app.models.votes import votes
class votes_repository:
    def __init__(self):
        pass
    
    def add_vote(self, user_id, poll_id,option):
        new_vote = votes(user_id=user_id, poll_id=poll_id, option=option)
        db.session.add(new_vote)
        db.session.commit()
