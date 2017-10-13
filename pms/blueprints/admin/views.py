# coding: utf-8
from flask import Blueprint, render_template
from flask_login import login_required

from pms.blueprints.user.models import User

admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')


@admin.route('/users', defaults={'page': 1})
@admin.route('/users/page/<int:page>')
@login_required
def index(page):
    users = User.query.paginate(page, per_page=15)

    return render_template('admin/user/index.html', users=users)