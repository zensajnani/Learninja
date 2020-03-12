from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from learninja import db, bp_student
from learninja.models import Topics
from learninja.mentor.forms import AddTopic, SearchTopic
import pandas as pd
import sqlite3


bp_mentor = Blueprint('bp_mentor', __name__)


@bp_mentor.route('/add-topic', methods=['GET', 'POST'])
def add_topic():
    form = AddTopic()
    course_add = subject_add = 'Other'
    topic_add = ''
    if form.validate_on_submit():
        if form.course_add.data:
            course_add = form.course_add.data
            if form.subject_add.data:
                subject_add = form.subject_add.data
        topic_add = form.topic_add.data
        add_topic_field = Topics(course=course_add, subject=subject_add, topic=topic_add)
        db.session.add(add_topic_field)
        db.session.commit()
        return redirect(url_for('bp_student.student'))
    return render_template('add-topic.html', form=form, course_add=course_add, subject_add=subject_add, topic_add=topic_add)


@bp_mentor.route('/mentor-profile', methods=['GET', 'POST'])
def mentor_profile():
    form = SearchTopic()
    topic_search = form.topic_search.data
    mentor_topic = Topics.query.filter_by(topic=topic_search).all()


    return render_template('mentor.html', form=form, mentor_topic=mentor_topic)