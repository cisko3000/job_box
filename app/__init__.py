import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ApplicationForm

from werkzeug import secure_filename

db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config['CSRF_SESSION_KEY'] = 'This is our secret key'
	app.config['SECRET_KEY'] = "cookie_secret_key"
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/job_box.db'
	app.config['UPLOAD_FOLDER'] = '/home/cisko/sites/job_box/app/resumes'
	app.config['ALLOWED_FILE_EXTENSIONS'] =set(['txt','pdf','doc','docx'])

	from models import Application

	db.init_app(app)


	def allowed_file(fname):
		if '.' in fname and fname.rsplit('.',1)[1] in app.config['ALLOWED_FILE_EXTENSIONS']:
			return True
		else:
			return False
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
			file = request.files['resume']
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				new_applicant = Application()
				form.populate_obj(new_applicant)
				new_applicant.resume = filename
				db.session.add(new_applicant)
				db.session.commit()
				return "Thanks for applying!"
			else:
				flash("Invalid file extension")
				return render_template('application.html', form=form)		
		return render_template('application.html', form=form)
	return app

