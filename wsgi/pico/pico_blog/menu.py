from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from pico_blog.models import Category

class CategoryMenu(CMSAttachMenu):
	name = _("Category Menu")

	def get_nodes(self, request):
		nodes = []
		for category in Category.objects.all().order_by('date_created'):
			node = NavigationNode(
				category.name,
				category.get_absolute_url(),
				category.id,
				)
			nodes.append(node)
		return nodes

menu_pool.register_menu(CategoryMenu)