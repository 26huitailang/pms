# coding: utf-8
from flask import Blueprint, render_template
from flask_login import login_required

from pms.blueprints.user.models import User

admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    users = User.query.all()

    return render_template('admin/user/index.html', users=users)