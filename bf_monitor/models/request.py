from bf_monitor import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    payg = db.Column(db.Boolean, nullable=False)
    paym = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Request available ({self.name})"