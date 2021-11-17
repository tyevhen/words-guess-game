from ..models import Card
import pickle

class Results:
    def __init__(self, cards):
        self.cards = cards
        self.current_card = self.cards[0]
        self.game_progress = {}
        self.card_progress = self.game_progress.get(self.current_card, {})
        for card in self.cards:
            self.game_progress[card] = {}
    
    def correct_answer(self):
        self.game_progress[self.current_card] = {
            'correct': self.game_progress[self.current_card].get('correct', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        self.cards.remove(self.current_card)
        self.current_card = self.cards[0]

    def wrong_answer(self):
        self.game_progress[self.current_card] = {
            'wrong': self.game_progress[self.current_card].get('wrong', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        if self.game_progress[self.current_card].get('attempts') < 3:
            self.cards += [self.cards.pop(0)]
        else:
            self.cards.remove(self.current_card)
        self.current_card = self.cards[0]

    def help_answer(self):
        self.game_progress[self.current_card] = {
            'help': self.game_progress[self.current_card].get('help', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        if self.game_progress[self.current_card].get('help') <= 2:
            self.cards.insert(2, self.cards.pop(0))
        else:
            self.cards.remove(self.current_card)
        self.current_card = self.cards[0]

    @property
    def serialize(self):
        return {
            'cards': self.cards,
            'current_card': self.current_card,
            'card_progress': self.card_progress,
            'game_progress': self.game_progress
        }

def save_game(game: Results):
    try:
        return pickle.dumps(game)
    except Exception as e:
        raise e


def load_game(binary):
    try:
        return pickle.loads(binary)
    except Exception as e:
        raise e
