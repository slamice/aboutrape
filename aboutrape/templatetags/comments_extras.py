from django import template

register = template.Library()

register.simple_tag

@register.filter(name='cssname')
def cssname(value):
    """Replaces all spaces with a dash to be a valid id for a cssname"""
    return value.replace(' ', '-')