from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """Cuts all the values of the Arguents from the text."""
    return value.replace(arg,"")