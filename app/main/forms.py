from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField, FileField,TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Length, EqualTo
from ..models import User,Blogs,Comment

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class FormBlog(FlaskForm):
    title = StringField('Blog Title', validators=[Required(), Length(1, 64)])
    author = StringField('Author : ',)
    content =TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Leave a comment ...', validators=[Required()])

    submit = SubmitField('Submit')
