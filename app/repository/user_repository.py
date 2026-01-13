from app.models.users import User
from app import db
class user_repository:
    def __init__(self):
        pass
    def add_user(self, new_user: User):
        db.session.add(new_user)
        db.session.commit()
    def get_user_by_id(self, user_id: str) -> User:
        exists=db.session.query(User).filter_by(user_id=user_id).first()
        if exists:
            return True
    def auth(self,user_id):
        user=db.session.query(User).filter_by(user_id=user_id).first()
        if not user:
            return False
        return user.password, user.salt
    def exists(self,user_id):
        user=db.session.query(User).filter_by(user_id=user_id).first()
        if user:
            return True
        return False
    