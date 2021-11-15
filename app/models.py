from flask_sqlalchemy import SQLAlchemy

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

class Game(db.Model):
    """ Guess game results model """
    __tablename__ = 'game'
    id = db.Column(db.Integer(), primary_key=True)
    player = db.Column(db.String(20))
