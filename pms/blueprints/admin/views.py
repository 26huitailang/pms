# coding: utf-8
from flask import Blueprint, render_template
from flask_login import login_required

from pms.blueprints.user.models import User
from pms.blueprints.admin.models import Dashboard


admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')


@admin.before_request
@login_required
def before_request():
    pass


@admin.route('/users', defaults={'page': 1})
@admin.route('/users/page/<int:page>')
def index(page):
    users = User.query.paginate(page, per_page=15)

    return render_template('admin/user/index.html', users=users)


@admin.route('')
def dashboard():
    group_and_count_users = Dashboard.group_and_count_users()

    return render_template('admin/page/dashboard.html',
                           group_and_count_users=group_and_count_users)