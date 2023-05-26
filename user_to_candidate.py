import sqlalchemy as sq
from model.base import Base


user_to_candidate = sq.Table(
    'user_to_candidate', Base.metadata,
    sq.Column('user_id', sq.Integer, sq.ForeignKey('user.id')),
    sq.Column('candidate_id', sq.Integer, sq.ForeignKey('candidate.id')),
)