import hashlib
import os
from datetime import datetime, timedelta
from app.repository.user_repository import user_repository
from app.models.users import User
from app.repository.poll_repository import poll_repository
from app.models.poll import poll
from app.models.PollOptions import PollOptions
from app.repository.votes_reppository import votes_repository
class service:
    @staticmethod
    def generate_salt():
        return os.urandom(16).hex()

    @staticmethod
    def hash_password(password, salt):
        return hashlib.sha256((password + salt).encode()).hexdigest()

    @staticmethod
    def add_user(user_id, password_hash, salt):
        repo = user_repository()
        try:
            new_user = User(user_id=user_id, password=password_hash, salt=salt)
            exists = repo.get_user_by_id(user_id)
            if exists:
                return {"error": "User already exists"}
            repo.add_user(new_user)
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    def create_poll(question, options):
        repo = poll_repository()
        new_poll = poll(question=question, options=options,closes=datetime.now()+ timedelta(days=1))
        poll_id = repo.add_poll(new_poll)
        return poll_id
    @staticmethod
    def get_poll(poll_id):
        repo = poll_repository()
        poll = repo.get_poll_by_id(poll_id)
        options=repo.get_options(poll_id)
        return poll, options
    @staticmethod
    def cast_vote(user_id,password,poll_id,option):
        user_repo=user_repository()
        hash, salt=user_repo.auth(user_id)
        if not hash or hash != service.hash_password(password,salt):
            return{'error':'authentication failed'}
        poll_repo =poll_repository()
        vote_repo=votes_repository()
        try:
            vote_repo.add_vote(user_id,poll_id,option)
        except Exception as e:
            return{'error':'user has already voted'}
        poll_repo.vote(poll_id,option)
        
        return {'message':'vote recorded'}
    @staticmethod
    def user_exists(user_id):
        user_repo=user_repository()
        return user_repo.exists(user_id)