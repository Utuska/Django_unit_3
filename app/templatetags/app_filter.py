from django.template import Library

register = Library()


@register.filter()
def color_app(value, arg='green'):
    if value == '-':
        arg = 'mistyrose'
        return arg
    if 2 > value > 1:
        arg = 'salmon'
    elif 5 > value > 2:
        arg = 'red'
    elif value > 5:
        arg = 'darkred'
    else:
        arg = 'springgreen'
    return arg