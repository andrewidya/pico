from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from pico_user_profile.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'User Profile'


class UserAdmin(UserAdmin):
	inlines = (UserProfileAdmin, )


	def get_queryset(self, request):
		user = getattr(request, 'user', None)

		qs = super(UserAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(id=user.id)

	def get_fieldsets(self, request, obj=None):
		if request.user.is_superuser:
			return super(UserAdmin, self).get_fieldsets(request, obj)
		return ((None, {'fields': ('username', 'password',)}), ('Personal Info', {'fields': ('first_name', 'last_name', 'email',)}))

admin.site.unregister(User)
admin.site.register(User, UserAdmin)