from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MentorSearch(FlaskForm):
    mentor_search = StringField(validators=[DataRequired()])
    search = SubmitField('Search')


class TopicSearch(FlaskForm):
    topic_search = StringField(validators=[DataRequired()])
    search = SubmitField('Search')


class AddTopic(FlaskForm):
    course_add = StringField()
    subject_add = StringField()
    topic_add = StringField(validators=[DataRequired()])
    search = SubmitField('Add')


