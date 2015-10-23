from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from pico_carousel.models import PicoCarousel, PicoCarouselItem
from django.utils.translation import ugettext_lazy as _

class PicoCarouselPlugin(CMSPluginBase):
	model = PicoCarousel
	module = _("Pico Carousel")
	name = _("Container")
	render_template = "pico_carousel/carousel.html"
	allow_children = True
	child_classes = ["PicoCarouselItemPlugin"]

	def render(self, context, instance, placeholder):
		context.update({
			'instance': instance,
			'placeholder':placeholder,
		})
		return context


class PicoCarouselItemPlugin(CMSPluginBase):
	model = PicoCarouselItem
	module = _("Carousel Item")
	name = _("Image Item")
	render_template = "pico_carousel/carousel_item.html"
	parent_classes = ["PicoCarouselPlugin"]
	allow_children = False

	def render(self, context, instance, placeholder):
		context.update({
			'instance': instance,
			'placeholder':placeholder,
		})
		return context

plugin_pool.register_plugin(PicoCarouselPlugin)
plugin_pool.register_plugin(PicoCarouselItemPlugin)
