import pickle

class GameHandler:
    def __init__(self, cards, task):
        self.cards = cards
        self.task = task
        self.is_valid = ''
        self.current_card = self.cards[0]
        self.game_progress = {}
        self.card_progress = self.game_progress.get(self.current_card, {})
        for card in self.cards:
            self.game_progress[card] = {}

    def validate_answer(self, answer):
        if answer.lower() == self.task.get('answer').lower():
            self.correct_answer()
            self.current_card = self.cards[0]
        if answer.lower() != self.task.get('answer').lower():
            self.wrong_answer()
        if answer.lower() == '':
            self.help_answer()
        self.task = None
    
    def correct_answer(self):
        self.is_valid = True
        self.game_progress[self.current_card] = {
            'correct': self.game_progress[self.current_card].get('correct', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        self.cards.remove(self.current_card)

    def wrong_answer(self):
        self.is_valid = False
        self.game_progress[self.current_card] = {
            'wrong': self.game_progress[self.current_card].get('wrong', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        if self.game_progress[self.current_card].get('attempts') < 3:
            self.cards += [self.cards.pop(0)]
        else:
            self.cards.remove(self.current_card)

    def help_answer(self):
        self.is_valid = None
        self.game_progress[self.current_card] = {
            'help': self.game_progress[self.current_card].get('help', 0) + 1,
            'attempts': self.game_progress[self.current_card].get('attempts', 0) + 1,
        }
        if self.game_progress[self.current_card].get('help') <= 2:
            self.cards.insert(2, self.cards.pop(0))
        else:
            self.cards.remove(self.current_card)

    @property
    def serialize(self):
        return {
            'cards': self.cards,
            'task': self.task,
            'current_card': self.current_card,
            'is_valid': self.is_valid,
            'card_progress': self.card_progress,
            'game_progress': self.game_progress
        }

def save_game(game: GameHandler):
    try:
        return pickle.dumps(game)
    except Exception as e:
        raise e


def load_game(binary):
    try:
        return pickle.loads(binary)
    except Exception as e:
        raise e
