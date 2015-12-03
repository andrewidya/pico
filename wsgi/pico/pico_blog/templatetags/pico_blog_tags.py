from django import template
from pico_blog.forms import SearchForm

register = template.Library()

@register.inclusion_tag('pico_blog/tags/search_form.html')
def search_form():
	search = SearchForm()
	return {'form': search}


