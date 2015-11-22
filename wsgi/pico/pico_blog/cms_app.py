from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from pico_blog.menu import CategoryMenu

class PicoBlogApp(CMSApp):
	name = _("Blog Application")
	urls = ['pico_blog.urls']
	app_name = 'pico_blog'
	menus = [CategoryMenu]

apphook_pool.register(PicoBlogApp)