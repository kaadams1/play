from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

    @classmethod
    def create(cls, email, password):
       """Create and return a new user."""

       return cls(email=email, password=password)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(User.email == email).first()

    @classmethod
    def all_users(cls):
        return cls.query.all()






# def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
#     flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
#     flask_app.config["SQLALCHEMY_ECHO"] = echo
#     flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     db.app = flask_app
#     db.init_app(flask_app)

#     print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    # connect_to_db(app)