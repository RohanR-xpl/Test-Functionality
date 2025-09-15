from extensions import db


class TestSuccess(db.Model):
    __tablename__ = 'test_success'

    id = db.Column(db.Integer, primary_key=True)
    success = db.Column(db.Boolean, default=False)
    name = db.Column(db.String)