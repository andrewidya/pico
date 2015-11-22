from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from pico_blog.models import Post, Category

class ArchivePostPlugin(CMSPluginBase):
	module = _("Pico Blog")
	name = _("Archive")
	models = CMSPlugin
	render_template = 'pico_blog/plugins/archive.html'

	def render(self, instance, context, placeholder):
		context = super(ArchivePostPlugin, self).render(instance, context, placeholder)
		context['post'] = Post.objects.order_by('-date_created')
		return context

class CategoryPlugin(CMSPluginBase):
	module = _("Pico Blog")
	name = _("Category")
	models = CMSPlugin
	render_template = 'pico_blog/plugins/category.html'

	def render(self, instance, context, placeholder):
		context = super(CategoryPlugin, self).render(instance, context, placeholder)
		context['categories'] = Category.objects.all()


plugin_pool.register_plugin(ArchivePostPlugin)
plugin_pool.register_plugin(CategoryPlugin)