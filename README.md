# words-guess-game

create database guess_game;
create user 'lingvist'@'localhost' identified by '1234';
grant all privileges on guess_game.* to 'lingvist'@'localhost';

export FLASK_APP=app
flask run