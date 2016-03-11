from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import ApplicationForm

db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config['CSRF_SESSION_KEY'] = 'This is our secret key'
	app.config['SECRET_KEY'] = "cookie_secret_key"
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/job_box.db'

	from models import Application

	db.init_app(app)

	@app.route('/')
	def index():
		return render_template('index.html')

	@app.route('/login')
	def login():
		return "LOGIN PAGE"

	@app.route('/apply',methods=['GET','POST'])
	def apply():
		form = ApplicationForm()
		if form.validate_on_submit():
			new_applicant = Application()
			form.populate_obj(new_applicant)
			new_applicant.resume = ''
			db.session.add(new_applicant)
			db.session.commit()
			return "Thanks for applying!"
		return render_template('application.html', form=form)
	return app

