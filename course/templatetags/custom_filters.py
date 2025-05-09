from django import template

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
