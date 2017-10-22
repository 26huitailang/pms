# coding: utf-8
from sqlalchemy import func

from pms.blueprints.user.models import User, db


class Dashboard(object):
    @classmethod
    def group_and_count_users(cls):
        """
        执行分组/统计所有用户数量

        :return: dict
        """
        return cls._group_and_count(User, User.role)

    @classmethod
    def _group_and_count(cls, model, field):
        """
        根据指定的model和field统计。

        :param model: Name of the model
        :type model: SQLAlchemy model
        :param field: Name of the field to group on
        :type field: SQLAlchemy field
        :return: dict
        """
        # 构建SQL函数表达式，为了计数各个field
        count = func.count(field)
        # 得到(数量, field)tuple 的列表
        query = db.session.query(count, field).group_by(field).all()

        results = {
            'query': query,
            'total': model.query.count()
        }

        return results
