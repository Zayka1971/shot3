import sqlalchemy as sq
from sqlalchemy.orm import relationship
from model.base import Base


class User(Base):
    __tablename__ = 'user'

    id = sq.Column(sq.Integer, primary_key=True)
    token = sq.Column(sq.String)
    candidates = relationship('Candidate', secondary='user_to_candidate')
