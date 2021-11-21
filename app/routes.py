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


@current_app.route('/game', methods=['GET', 'POST'])
def game():
    active_game = Game.query.filter(Game.ended_at == None).order_by(desc(Game.started_at)).first()
    if active_game:
        print("UNFINISHED GAME")
        game_handler = load_game(active_game.results)
    else:
        print("NEW GAME")
        cards = Card.query.all()  
        card_ids = [card.id for card in cards]
        game_handler = GameHandler(card_ids, cards[0].task)
        active_game = Game(results=save_game(game_handler))
        commit_to_db(active_game)

    if request.method == 'GET':    
        print("LOAD GAME TASK", game_handler.task)
        return jsonify(game_handler.serialize)
    
    if request.method == 'POST':
        print("REQ: ", request.data)
        answer = request.args.get('answer')
        print("CLIENT ANSWER: ", answer)
        game_handler.validate_answer(answer)
        print("CURR CARD\n\n", game_handler.current_card)
        next_card = Card.query.filter(Card.id == game_handler.current_card).one()
        game_handler.task = next_card.task
        print("PROGRESS", game_handler.game_progress)
        active_game.results = save_game(game_handler)
        db.session.commit()

        return jsonify(game_handler.serialize)
    

# @current_app.route('/card', methods=['GET'])
# def get_cards():
#     cards = Card.query.all()

#     return jsonify([card.serialize for card in cards])
