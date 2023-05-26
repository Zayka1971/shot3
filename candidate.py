import sqlalchemy as sq
from sqlalchemy.orm import relationship
from model.base import Base


class Candidate(Base):
    __tablename__ = 'candidate'

    id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    screen_name = sq.Column(sq.String)
    photos = relationship('Photo', backref='candidate')
    users = relationship('User', secondary='user_to_candidate')
