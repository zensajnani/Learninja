from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from learninja import db
from learninja.models import Users
from learninja.account.forms import SignupForm, LoginForm, ToggleMentorMode

users = Blueprint('users', __name__)


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user = Users(username=form.username.data, email=form.email.data, password=form.password.data, user_type=1)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('signup.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(url_for('users.profile'))
    return render_template('login.html', form=form)


@users.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ToggleMentorMode()
    if form.validate_on_submit():
        if current_user.user_type == 1:
            current_user.user_type = 2
            db.session.commit()
        else:
            current_user.user_type = 1
            db.session.commit()
    return render_template('profile.html', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users.route('/become-mentor')
@login_required
def become_mentor():
    current_user.user_type = 2
    db.session.commit()
    return redirect(url_for('users.profile'))

@users.route('/test')
def test():
    return render_template('test.html', form=form)

