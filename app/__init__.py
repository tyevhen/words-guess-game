from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lingvist:1234@localhost/guess_game'
    
    from .models import db
    migrate = Migrate()    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes
        return app

