# coding: utf-8
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from flask import request


def safe_next_url(target):
    """
    保证相对路径在同样的域中。
    保护开放重定向的漏洞。

    :param target: Relative url (通常由flask-login提供)
    :return: str
    """
    return urljoin(request.host_url, target)
