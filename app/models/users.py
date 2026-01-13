from dataclasses import dataclass
from app import db
@dataclass
class User(db.Model):
    user_id: str
    password: str
    salt: str
    __tablename__ = 'users'
    user_id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)
    salt = db.Column(db.String(32), nullable=False)