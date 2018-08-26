from bf_monitor import db


class TestUser(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    type = db.Column(db.String(4), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Test data ({self.username}, {self.password}, {self.type})"

    def get_paym_list(user_id):
        return TestUser.query.filter_by(user_id=user_id).filter_by(type='PAYM').all()

    def get_payg_list(user_id):
        return TestUser.query.filter_by(user_id=user_id).filter_by(type='PAYG').all()

