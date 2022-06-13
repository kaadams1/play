from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # write a function that creates a game and adds it to the database.
    Game.query.delete()

    sg = Game(name='SuperAwesomeFun game', description='One player to rule them all')
    sh = Game(name='PLAYME', description='You know you want to')
    sf = Game(name='Fantastic Beasts', description='Catch a really cool monster')

    db.session.add_all([sg, sh, sf])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
