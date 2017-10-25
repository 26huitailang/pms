# coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, flash
from pms.blueprints.user.models import User
from flask_login import login_user, logout_user, login_required

from lib.safe_next_url import safe_next_url

from pms.blueprints.user.forms import LoginForm

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/')
def index():
    return redirect(url_for('admin.index'))


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(next=request.args.get('next'))

    if form.validate_on_submit():
        u = User.find_by_identity(request.form.get('identity'))

        if u and u.authenticated(password=request.form.get('password')):

            if login_user(u, remember=request.form.get('remember_me')) and u.is_active():
                next_url = request.form.get('next')
                print(">>redirect next_url: {}".format(next_url))
                if next_url:
                    return redirect(safe_next_url(next_url))
                return redirect(url_for('admin.index'))
            else:
                flash('This account has been disabled.', 'error')
        else:
            flash('Identity or password is incorrect.', 'error')

    return render_template('user/login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('user.login'))