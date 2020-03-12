from learninja import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.Text, index=True, nullable=True)
    username = db.Column(db.Text, unique=True, index=True)
    email = db.Column(db.Text, unique=True, index=True)
    password_hash = db.Column(db.Text)
    user_type = db.Column(db.Integer)

    # profile_image = db.Column(db.Text, nullable=True)

    def __init__(self, username, email, password, user_type):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.user_type = user_type

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Username: {self.username}'


class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Text, index=True)
    subject = db.Column(db.Text, index=True)
    topic = db.Column(db.Text, index=True)

    def __init__(self, course, subject, topic):
        self.course = course
        self.subject = subject
        self.topic = topic

    def __repr__(self):
        return f'{self.course}-{self.subject}-{self.topic}'

