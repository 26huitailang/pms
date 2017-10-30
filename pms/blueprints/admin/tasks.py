# coding: utf-8
from pms.app import create_celery_app

from pms.blueprints.user.models import User

celery = create_celery_app()


@celery.task()
def delete_users(ids):
    """
    删除用户。

    :param ids: 需要删除的用户
    :type ids: list
    :return: int
    """
    return User.bulk_delete(ids)
