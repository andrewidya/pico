from django.conf.urls import patterns, url
from pico_blog.views import PostListView, PostDetailView, CategoryListView, PostArchiveListView, TagListView, AuthorPostListView, search, results

urlpatterns = patterns (
	'',
	url(r'^$', PostListView.as_view(), name='post-list'),
	url(r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$', PostDetailView.as_view(), name='post-detail'),
	url(r'^category/(?P<category>[\w\.@+-]+)/$', CategoryListView.as_view(), name='category-post-list'),
	url(r'^(?P<year>\d{4})/$', PostArchiveListView.as_view(), name='archive-post-list'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostArchiveListView.as_view(), name='archive-post-list'),
	url(r'^tag/(?P<tag>[-\w]+)/$', TagListView.as_view(), name='tag-post-list'),
	url(r'^author/(?P<username>[\w\.@+-]+)/$', AuthorPostListView.as_view(), name='author-post-list'),
	url(r'^search/$', search, name='search'),
)