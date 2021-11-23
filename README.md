# words-guess-game server

1. create database guess_game;
   create user 'lingvist'@'localhost' identified by '1234';
   grant all privileges on guess_game.* to 'lingvist'@'localhost';

2. pip install virtualenv
3. virtualenv venv
4. source venv/bin/activate
5. pip install requirements.txt
6. flask db upgrade
7. export FLASK_APP=app
8. flask run