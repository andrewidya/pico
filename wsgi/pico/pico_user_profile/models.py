from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	avatar = FilerImageField(verbose_name="Profile Picture", blank=True, null=True, on_delete=models.SET_NULL)
	home_address = models.CharField(max_length=100, verbose_name="Address", blank=True, null=True)
	state = models.CharField(max_length=20, help_text="State/Province", blank=True, null=True)
	city = models.CharField(max_length=20, help_text="City", blank=True, null=True)
	phone_number = models.CharField(max_length=12, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)