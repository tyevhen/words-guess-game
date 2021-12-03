from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func
import editdistance
import string

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
    def task(self):
        form_translation_clean = self.form_translation.translate(
            str.maketrans('', '', string.punctuation)).lower().split(' ')
        context_translation_clean = self.context_translation.translate(
            str.maketrans('', '', string.punctuation)).split(' ')

        print('form_translation_clean', form_translation_clean)
        print('context_translation_clean', context_translation_clean)

        lowest_distance = 1000
        word_task = ''

        for word in context_translation_clean:
            distances = [editdistance.eval(
                word.lower(), x) for x in form_translation_clean]
            word_candidate_from_translation = form_translation_clean[
                distances.index(min(distances))]
            curr_lowest_dist = min(distances)
            if curr_lowest_dist < lowest_distance and word_candidate_from_translation[0] == word[0].lower():
                lowest_distance = curr_lowest_dist
                word_task = word

        task = {
            'phrase_template': self.context_translation.replace(word_task, '*'),
            'answer': word_task,
            'card': self.serialize
        }
        print("TASKKK", task)
        return task

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
