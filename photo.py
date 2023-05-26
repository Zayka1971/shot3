import sqlalchemy as sq
from model.base import Base


class Photo(Base):
    __tablename__ = 'photo'

    # "<type><owner_id>_<media_id>"
    id = sq.Column(sq.String, primary_key=True)
    photo_id = sq.Column(sq.Integer)
    candidate_id = sq.Column(sq.Integer, sq.ForeignKey('candidate.id'))
    likes_count = sq.Column(sq.Integer)
    comments_count = sq.Column(sq.Integer)
