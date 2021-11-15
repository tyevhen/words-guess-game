from flask import current_app

@current_app.route('/')
def index():
    # return result.task_id, 200
    return "I'm index!"

# @current_app.route('/game')
# def game():
    