from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()

class Card(db.Model):
    """ Guess card model """
    __tablename__ = 'card'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    priority = db.Column(db.Integer())
    word = db.Column(db.String(100), nullable=False)
    phrase_tag = db.Column(db.String(3), nullable=False)
    context = db.Column(db.String(100), nullable=False)
    form_translation = db.Column(db.String(100), nullable=False)
    context_translation = db.Column(db.String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'priority': self.priority,
            'word': self.word,
            'phrase_tag': self.phrase_tag,
            'context': self.context,
            'form_translation': self.form_translation,
            'context_translation': self.context_translation
        }

class Game(db.Model):
    """ Guess game results model """
    __tablename__ = 'game'
    id = db.Column(db.Integer(), primary_key=True)
    results = db.Column(db.LargeBinary)
    started_at = db.Column(DateTime, default=func.now())
    ended_at = db.Column(DateTime, nullable=True)

    # @property
    # def serialize(self):

