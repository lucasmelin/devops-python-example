from django import template

register = template.Library()


@register.filter(name='addCssClass')
def add_css_class(value, arg):
    return value.as_widget(attrs={'class': arg})
