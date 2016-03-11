from flask.ext.wtf import Form

from wtforms.validators import Required
from wtforms import TextField, FileField, SubmitField



class ApplicationForm(Form):
	first_name = TextField("First Name")
	last_name = TextField("Last Name")
	email = TextField("Email", [Required()])
	resume = FileField("Resume")

	submit = SubmitField("Apply")
