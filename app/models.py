from . import db

class Application(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(32))
	last_name = db.Column(db.String(32))
	email = db.Column(db.String(32))
	resume = db.Column(db.String())


