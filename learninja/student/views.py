from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from learninja import db
from learninja.models import Topics
from learninja.student.forms import MentorSearch, TopicSearch

bp_student = Blueprint('bp_student', __name__)


@bp_student.route('/student', methods=['GET', 'POST'])
def student():
    form = TopicSearch()
    subject_topic = ''
    course_topic = ''
    if form.validate_on_submit():
        topic_search_field = Topics.query.filter_by(topic=form.topic_search.data).first()
        subject_topic = topic_search_field.subject
        course_topic = topic_search_field.course
    return render_template('student.html', form=form, subject_topic=subject_topic, course_topic=course_topic)


@bp_student.route('/mentor-search', methods=['GET', 'POST'])
def mentor_search():
    form = MentorSearch()
    return render_template('mentor-search.html', form=form)

