from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from taggit_autosuggest.managers import TaggableManager

# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
	date_created = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
	date_modified = models.DateTimeField(verbose_name=_('Modified at'), default=timezone.now)
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), blank=True, db_index=True)

	class Meta:
		verbose_name = _("Blog Category")
		verbose_name_plural = _("Blog Categories")

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
			self.date_created = timezone.now()
		self.date_modified = timezone.now()
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('pico_blog:category-post-list', kwargs={'category': self.slug})

@python_2_unicode_compatible
class Post(models.Model):
	author = models.ForeignKey(User, null=True, blank=True)
	date_created = models.DateTimeField(_(u'created'), auto_now_add=True)
	date_modified = models.DateTimeField(_(u'last modified'), default=timezone.now)
	date_published = models.DateTimeField(_(u'published Since'), default=timezone.now)
	date_published_end = models.DateTimeField(_(u'published Until'), null=True, blank=True)
	publish = models.BooleanField(default=False)
	categories = models.ManyToManyField(Category, verbose_name=_("Category"), related_name="blog_posts")
	feature_image = FilerImageField(verbose_name=_("Feature Image"), blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(verbose_name=_("Title"), max_length=255)
	slug = models.SlugField(verbose_name=_("Slug"), blank=True, db_index=True)
	post_intro = models.TextField(verbose_name=_("Post Intro"), max_length=255, blank=True, null=True)
	meta_description=models.TextField(verbose_name=_(u'post meta description'), blank=True, default='')
	meta_keywords=models.TextField(verbose_name=_(u'post meta keywords'), blank=True, default='')
	meta_title=models.CharField(verbose_name=_(u'post meta title'), help_text=_(u'used in title tag and social sharing'),max_length=255, blank=True, default='')
	post_content = HTMLField(_(u'Content'), default='', blank=True)
	tags = TaggableManager(blank=True)
	javansese_text = models.BooleanField(default=True)

	_metadata = {
		'tag': 'get_tags',
	}

	class Meta:
		verbose_name = _("Blog Article")
		verbose_name_plural = _("Blog Articles")
		ordering = ('-date_published', '-date_created')
		get_latest_by = 'date_published'

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug and self.title:
			self.slug = slugify(self.title)
			self.date_created = timezone.now()
		self.date_modified = timezone.now()
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		kwargs = {
			'year': self.date_published.year,
			'month': '%02d' % self.date_published.month,
			'day': '%02d' % self.date_published.day,
			'slug': self.slug
		}
		return reverse('pico_blog:post-detail', kwargs=kwargs)

	def get_tags(self):
		taglist = [tag.name for tags in self.tags.all()]
		return ','.join(taglist)

	def is_javanese(self):
		if self.javansese_text:
			return True
		return False

	def has_post_intro(self):
		if self.post_intro:
			return True
		return False

	def has_feature_image(self):
		if self.feature_image:
			return True
		return False

class BlogSetting(models.Model):
	pass