from flask import current_app, request, jsonify
from sqlalchemy import desc
from .services.game import Results, load_game, save_game
from .models import Card, Game, db


def commit_to_db(entry):
    try:
        db.session.add(entry)
        db.session.commit()
        return entry.id
    except Exception as e:
        raise e


@current_app.route('/', methods=['GET', 'POST'])
def game():
    cards = Card.query.all()  
    active_game = Game.query.filter(Game.ended_at == None).order_by(desc(Game.started_at)).first()
    if active_game:
        print("UNFINISHED GAME")
        result = load_game(active_game.results)
    else:
        print("NEW GAME")
        card_ids = [card.id for card in cards]
        result = Results(card_ids)
        active_game = Game(results=save_game(result))
        commit_to_db(active_game)

    if request.method == 'GET':    
        return jsonify(result.serialize)
    
    if request.method == 'POST':
        answer = request.args.get('answer')
        if answer == 'correct':
            result.correct_answer()
            
        elif answer == 'wrong':
            result.wrong_answer()
        
        elif answer == 'help':
            result.help_answer()
        print("ANSWER", result.game_progress)
        print("CARD ORDER", result.cards)

        active_game.results = save_game(result)
        db.session.commit()

        return {}
    
    return "I'm index!"

@current_app.route('/card', methods=['GET'])
def get_cards():
    cards = Card.query.all()

    return jsonify([card.serialize for card in cards])
