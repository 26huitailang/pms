# coding: utf-8
from flask_wtf import Form


class ModelForm(Form):
    """
    wtforms构成里有ModelForm，但是不继承自flask_wtf的Form而是WTForms的Form。

    然而，为了能得到CSRF保护，我们需要让他继承flask_wtf的Form，这里直接复制它的类。

    我们通过移除它的format参数，这样以便wtforms组件能自动将值传递到request.form。
    """
    def __init__(self, obj=None, prefix='', **kwargs):
        Form.__init__(self, obj=obj, prefix=prefix, **kwargs)

        self._obj = obj


def choices_from_dict(source, prepend_blank=True):
    """
    将dict转变为适应WTForms的选项。预设了"请选择一项..."的值。

    Example:
        # Convert this data structure:
        ROLE = OrderedDict([
            ('member', 'Member'),
            ('manager', 'Manager'),
            ('boss', 'Boss'),
            ('admin', 'Admin')
        ])
        # Into this:
        choices = [('', '请选择一项...', ('member', 'Member')...]

    :param source: Input source
    :type source: dict
    :param prepend_blank: An optional blank item
    :type prepend_blank: bool
    :return: list
    """
    choices = []

    if prepend_blank:
        choices.append(('', '请选择一项...'))

    for key, value in source.items():
        pair = (key, value)
        choices.append(pair)

    return choices
