from bf_monitor import db, login_manger
from flask_login import UserMixin

@login_manger.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), unique=True, nullable=False)
    test_data = db.relationship('TestUser', backref='creator', lazy=True)

    def __repr__(self):
        return f"User ({self.username}, {self.password}, {self.email}, {self.image_file})"

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


