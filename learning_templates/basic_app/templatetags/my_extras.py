from django import template

register = template.Library() #1 st method to register

#2nd method via decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    this cuts out all values of "args from the string!"
    """
    return value.replace(arg, '')

#register.filter regd for 1st method
#register.filter('cut',cut)

#1st cut is name of the filter we kept 2nd is the function name
