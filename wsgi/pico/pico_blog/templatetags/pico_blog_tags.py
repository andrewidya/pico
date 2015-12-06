from django import template
from pico_blog.forms import SearchForm

register = template.Library()

@register.inclusion_tag('pico_blog/tags/search_form.html')
def search_form():
	search = SearchForm()
	return {'form': search}

@register.filter(name='is_mod')
def is_mod(value, arg):
	if value % arg == 0:
		return True
	return False