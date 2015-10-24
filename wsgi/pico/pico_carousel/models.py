from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings
from filer.fields.image import FilerImageField

# Create your models here.
@python_2_unicode_compatible
class PicoCarousel(CMSPlugin):
	def __str__(self):
		return _(u"%s items") % self.cmsplugin_set.all().count()

@python_2_unicode_compatible
class PicoCarouselItem(CMSPlugin):
	image = FilerImageField(null=True, blank=True)
	img_alt = models.CharField(_("Image alternate attribute"), max_length=100)
	title_caption = models.CharField(_("Caption Title"), max_length=100)
	desc_caption = models.CharField(_("Caption Description"), max_length=250)

	def __str__(self):
		return _(u"%s") % self.title_caption
