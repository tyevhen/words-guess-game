from datetime import datetime
from flask import current_app, request, jsonify
from sqlalchemy import desc
from .services.game_handler import GameHandler, load_game, save_game
from .models import Card, Game, db


def commit_to_db(entry):
    try:
        db.session.add(entry)
        db.session.commit()
        return entry.id
    except Exception as e:
        raise e

def create_new_game():
    cards = Card.query.all()  
    card_ids = [card.id for card in cards]
    game_handler = GameHandler(card_ids, cards[0].task)
    active_game = Game(results=save_game(game_handler))
    commit_to_db(active_game)
    return game_handler


@current_app.route('/game', methods=['GET', 'POST'])
def game():
    active_game = Game.query.filter(Game.ended_at == None).order_by(desc(Game.started_at)).first()
    if active_game:
        print("UNFINISHED GAME")
        game_handler = load_game(active_game.results)
    else:
        print("NEW GAME")
        game_handler = create_new_game()

    if request.method == 'GET':    
        return jsonify(game_handler.serialize)
    
    if request.method == 'POST':
        answer = request.args.get('answer')
        print("CLIENT ANSWER: ", answer)
        game_handler.validate_answer(answer)
        if not game_handler.finished:
            next_card = Card.query.filter(Card.id == game_handler.current_card).one()
            game_handler.task = next_card.task
            active_game.results = save_game(game_handler)
            db.session.commit()
        else:
            active_game.ended_at = datetime.now()
            db.session.commit()
        
        return jsonify(game_handler.serialize)

        
    