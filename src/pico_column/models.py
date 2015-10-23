from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings

# Create your models here.
if hasattr(settings, "PICO_COLUMN_WIDTH_CHOICES"):
    WIDTH_CHOICES = settings.COLUMN_WIDTH_CHOICES
else:
    WIDTH_CHOICES = (
        ('1', _("1/12")),
        ('2', _("2/12")),
        ('3', _("3/12")),
        ('4', _("4/12")),
        ('5', _("5/12")),
        ('6', _("6/12")),
        ('7', _("7/12")),
        ('8', _("8/12")),
        ('9', _("9/12")),
        ('10', _("10/12")),
        ('11', _("11/12")),
        ('12', _("12/12")),
    )

@python_2_unicode_compatible
class PicoRow(CMSPlugin):
	def __str__(self):
		return _(u"%s columns") % self.cmsplugin_set.all().count()

@python_2_unicode_compatible
class PicoColumn(CMSPlugin):
	large_width = models.CharField(_("large width"), choices=WIDTH_CHOICES, default=WIDTH_CHOICES[0][0], max_length=50, help_text="Width size used for large devices *col-lg-??")
	medium_width = models.CharField(_("medium width"), choices=WIDTH_CHOICES, default=WIDTH_CHOICES[0][0], max_length=50, help_text="Width size used for medium devices *col-md-??")
	small_width = models.CharField(_("small width"), choices=WIDTH_CHOICES, default=WIDTH_CHOICES[0][0], max_length=50, help_text="Width size used for small device *col-sm-??")
	extra_small_width = models.CharField(_("extra small width"), choices=WIDTH_CHOICES, default=WIDTH_CHOICES[0][0], max_length=50, help_text="Width size used for extra small device *col-sm-??")

	def __str__(self):
		return u"Large %s, Medium %s, Small %s, Extra Small %s" % (self.large_width, self.medium_width, self.small_width, self.extra_small_width)