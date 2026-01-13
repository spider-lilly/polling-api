from app import db
from app.models.poll import poll
from sqlalchemy import text
from app.models.PollOptions import PollOptions
class poll_repository:
    def __init__(self):
        pass
    def add_poll(self, new_poll: poll):
        db.session.add(new_poll)
        db.session.commit()
        self.add_polloptions(new_poll.options, new_poll.poll_id)
        return new_poll.poll_id
    def get_poll_by_id(self, poll_id: int) -> poll:
        return db.session.query(poll).filter_by(poll_id=poll_id).first()
    def add_polloptions(self,options,poll_id):
        for option_text in options:
            option = PollOptions(poll_id=poll_id, option_text=option_text)
            db.session.add(option)
        db.session.commit()
    def get_options(self, poll_id):
        return db.session.execute(
            text("""SELECT option_id, option_text, votes FROM poll_options WHERE poll_id = :poll_id"""),
            {"poll_id": poll_id}
        ).fetchall()
    def vote(self, poll_id,option):
        db.session.execute(
            text("""UPDATE poll_options SET votes = votes + 1 WHERE poll_id = :poll_id AND option_text = :option"""),
            {"poll_id": poll_id, "option": option}
        )
        db.session.commit()
        return "vote recorded"