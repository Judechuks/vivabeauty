# custom_filters.py - function that formats integers with commas.
# this file nedd to be saved in the templatetags folder same root as the app folder

from django import template

register = template.Library()

@register.filter
def format_with_commas(value):
  return f"{value:,}"
