import pickle


class GameHandler:
    def __init__(self, cards, task):
        self.cards = cards
        self.task = task
        self.is_valid = ''
        self.finished = False
        self.card = self.cards[0]
        self.progress = {}
        for card in self.cards:
            self.progress[card] = {}

    def validate_answer(self, answer):
        self.progress[self.card]['attempts'] = self.progress[self.card].get(
            'attempts', 0) + 1
        if answer.lower() == '':
            self.help_answer()
        elif answer.lower().strip() == self.task.get('answer').lower():
            self.correct_answer()
            if len(self.cards) == 0:
                self.finished = True
            else:
                self.card = self.cards[0]
        elif answer.lower().strip() != self.task.get('answer').lower():
            self.wrong_answer()
        self.task = None

    def correct_answer(self):
        self.is_valid = True
        self.progress[self.card]['correct'] = self.progress[self.card].get(
            'correct', 0) + 1
        self.cards.remove(self.card)

    def wrong_answer(self):
        self.is_valid = False
        self.progress[self.card]['wrong'] = self.progress[self.card].get(
            'wrong', 0) + 1
        if self.progress[self.card].get('attempts') < 3:
            self.cards += [self.cards.pop(0)]
        # else:
        #     self.cards.remove(self.card)

    def help_answer(self):
        self.is_valid = None
        self.progress[self.card]['help'] = self.progress[self.card].get(
            'help', 0) + 1
        if self.progress[self.card]['help'] <= 2:
            self.cards.insert(2, self.cards.pop(0))
        # else:
        #     self.cards.remove(self.card)

    @property
    def serialize(self):
        return {
            'cards': self.cards,
            'task': self.task,
            'card': self.card,
            'is_valid': self.is_valid,
            'card_progress': self.progress.get(
                self.card,
                {'attempts': 0, 'help': 0, 'wrong': 0, 'correct': 0}),
            'game_progress': self.progress,
            'finished': self.finished
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
