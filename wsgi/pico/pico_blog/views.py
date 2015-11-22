from django.shortcuts import render
from django.views.generic import DetailView, ListView
from pico_blog.models import Post, Category
from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve
from django.utils.timezone import now

User = get_user_model()

class PostListView(ListView):
	model = Post
	context_object_name = 'post_list'
	queryset = Post.objects.all()
	view_url_name = 'pico_blog:post-list'
	template_name = 'pico_blog/post_list.html'
	paginated_by = 20

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'pico_blog/post_detail.html'
	view_url_name = 'pico_blog:post-detail'
	slug_field = 'slug'

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		return context

class CategoryListView(ListView):
	model = Post
	context_object_name = 'post_list'
	template_name = 'pico_blog/post_list.html'
	view_url_name = 'pico_blog:category-post-list'

	def get_queryset(self):
		qs = super(CategoryListView, self).get_queryset()
		if 'category' in self.kwargs:
			qs = qs.filter(categories__slug=self.kwargs['category'])
		return qs

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		return context

class PostArchiveListView(ListView):
	model = Post
	context_object_name = 'post_list'
	template_name = 'pico_blog/archive_list.html'
	view_url_name = 'pico_blog:archive-post-list'
	date_field = 'date_published'

	def get_queryset(self):
		qs = super(PostArchiveListView, self).get_queryset()
		if 'month' in self.kwargs:
			qs = qs.filter(**{'%s__month' % self.date_field: self.kwargs['month']})
		if 'year' in self.kwargs:
			qs = qs.filter(**{'%s__year' % self.date_field: self.kwargs['year']})
		return qs

	def get_context_data(self, **kwargs):
		kwargs['month'] = int(self.kwargs.get('month')) if 'month' in self.kwargs else None
		kwargs['year'] = int(self.kwargs.get('year')) if 'year' in self.kwargs else None
		if kwargs['year']:
			kwargs['archive_date'] = now().replace(kwargs['year'], kwargs['month'] or 1, 1)
		context = super(PostArchiveListView, self).get_context_data(**kwargs)
		return context

class TagListView(ListView):
	model = Post
	context_object_name = 'post_list'
	template_name = 'pico_blog/tag_list.html'
	view_url_name = 'pico_blog:tag-post-list'

	def get_queryset(self):
		qs = super(TagListView, self).get_queryset()
		return qs.filter(tags__slug=self.kwargs['tag'])

	def get_context_data(self, **kwargs):
		context = super(TagListView, self).get_context_data(**kwargs)
		return context

class AuthorPostListView(ListView):
	model = Post
	context_object_name = 'post_list'
	template_name = 'pico_blog/author_post_list.html'
	view_url_name = 'pico_blog:author-post-list'

	def get_queryset(self):
		qs = super(AuthorPostListView, self).get_queryset()
		if 'username' in self.kwargs:
			qs = qs.filter(**{'author__%s' % User.USERNAME_FIELD: self.kwargs['username']})
		return qs

	def get_context_data(self, **kwargs):
		kwargs['author'] = User.objects.get(**{User.USERNAME_FIELD: self.kwargs.get('username')})
		context = super(AuthorPostListView, self).get_context_data(**kwargs)
		return context