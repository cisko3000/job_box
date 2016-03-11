from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, FileField, SubmitField
from wtforms.validators import Required

class ApplicationForm(Form):
	first_name = TextField("First Name")
	last_name = TextField("Last Name")
	email = TextField("Email", [Required()])
	resume = FileField("Resume")

	submit = SubmitField("Apply")

