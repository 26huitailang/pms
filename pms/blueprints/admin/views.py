# coding: utf-8
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required

from pms.blueprints.user.models import User
from pms.blueprints.admin.models import Dashboard

from pms.blueprints.admin.forms import BulkDeleteForm, UserForm, SearchForm

admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')


# @admin.before_request
# @login_required
# def before_request():
#     pass


@admin.route('/')
@admin.route('/index')
def index():
    group_and_count_users = Dashboard.group_and_count_users()

    return render_template('admin/page/dashboard.html',
                           group_and_count_users=group_and_count_users)


@admin.route('/projects')
def projects():
    return 'Projects'


@admin.route('/users', defaults={'page': 1})
@admin.route('/users/page/<int:page>')
def users(page):
    search_form = SearchForm()

    paginated_users = User.query \
        .filter(User.search(request.args.get('q', ''))) \
        .paginate(page, per_page=15, error_out=True)

    return render_template('admin/user/users.html', users=paginated_users,
                           form=search_form)


@admin.route('/users/bulk_delete', methods=['POST'])
def users_bulk_delete():
    form = BulkDeleteForm()

    pass


@admin.route('/users/delete/<int:id>')
def users_one_delete(id):
    from pms.blueprints.admin.tasks import delete_users

    delete_users([id])

    flash('{0} user(s) were scheduled to be deleted.'.format(len([id])), 'success')

    return redirect(url_for('admin.users'))


@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
def users_edit(id):
    user = User.query.get(id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        # TODO 判定最后一个管理员

        form.populate_obj(user)

        user.save()

        flash('用户保存成功。', 'success')
        return redirect(url_for('admin.users'))

    return render_template('admin/user/edit.html', form=form, user=user)


@admin.route('/users/new', methods=['GET', 'POST'])
def users_new():
    user = User()
    form = UserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)

        user.save()

        flash('用户添加成功。', 'success')
        return redirect(url_for('admin.users'))

    return render_template('admin/user/edit.html', form=form, user=user)

