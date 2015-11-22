from django.contrib import admin
from pico_blog.models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'date_created', 'date_modified')

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date_created', 'date_modified', 'publish')
	list_editable = ('publish',)
	fieldsets = (
		('Blog Post', {
			'fields': ('title', 'slug', 'post_intro', 'post_content', 'categories', 'tags', 'javansese_text' )
			}),
		('Post Feature Image', {
			'fields': ('feature_image',)
			}),
		('Date Information', {
			'fields': ('date_published', 'date_published_end')
			}),
		('SEO', {
			'fields': ('meta_title', 'meta_description', 'meta_keywords'),
			'classes': ('collapse',)
			}),
	)

	def save_model(self, request, obj, form, change):
		if not obj.author:
			obj.author = request.user
			obj.save()
		super(PostAdmin, self).save_model(request, obj, form, change)

	def get_list_display(self, request):
		if request.user.is_superuser:
			return super(PostAdmin, self).get_list_display(request)
		return ('title', 'author', 'date_created', 'date_modified')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)