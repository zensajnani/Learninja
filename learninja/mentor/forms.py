from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class AddTopic(FlaskForm):
    course_add = StringField()
    subject_add = StringField()
    topic_add = StringField(validators=[DataRequired()])
    search = SubmitField('Add Topic')


class SearchTopic(FlaskForm):
    topic_search = StringField(validators=[DataRequired()])
    search = SubmitField('Search')
    add = SubmitField('Add')


class MentorAddTopic(FlaskForm):
    select_topic = BooleanField()
    add = SubmitField('Add')