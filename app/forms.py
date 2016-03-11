from flask.ext.wtf import Form
<<<<<<< HEAD
from wtforms.fields import TextField, TextAreaField, FileField, SubmitField
from wtforms.validators import Required
=======
from wtforms import TextField, FileField, SubmitField
>>>>>>> e1feb23c3c8f878fe304416a049bb1d15ff2964e

class ApplicationForm(Form):
	first_name = TextField("First Name")
	last_name = TextField("Last Name")
<<<<<<< HEAD
	email = TextField("Email", [Required()])
	resume = FileField("Resume")

	submit = SubmitField("Apply")

=======
	email = TextField("Email")
	resume = FileField("Resume")

	submit = SubmitField('Apply')
>>>>>>> e1feb23c3c8f878fe304416a049bb1d15ff2964e
