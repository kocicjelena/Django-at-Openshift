from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
#from django.conf.urls import patterns
from Blog import views
from . import Blog
from Blog.views import *
#from Blog.views import posts, search, searchform, i, searchh, MyView, BookListView, bloglist, item_edit, authorlist, entry, contact, contact2, contact3, searchblog
#from Blog.models import Blog, Author, Entry
#from Blog.views import posts
#from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
	url(r'^index/', 'openshift.views.index', name='index'),
	url(r'^blog/index/', 'openshift.Blog.views.posts', name='posts'),
	url(r'^blog/authorlist/', 'openshift.Blog.views.authorlist', name='authorlist'),
	url(r'^blog/bloglist/', 'openshift.Blog.views.bloglist', name='bloglist'),
	url(r'^blog/searchform/', 'openshift.Blog.views.searchform', name='searchform'),
	url(r'^blog/posts/', 'openshift.Blog.views.posts', name='posts'),
	url(r'^blog/search/', 'openshift.Blog.views.search', name='search'),
	url(r'^blog/searchh/', 'openshift.Blog.views.searchh', name='searchh'),
	url(r'^blog/i/', 'openshift.Blog.views.i', name='i'),
	url(r'^blog/itemedit/', 'openshift.Blog.views.itemedit', name='itemedit'),
	url(r'^blog/entry/', 'openshift.Blog.views.entry', name='entry'),
	url(r'^blog/searchblog/', 'openshift.Blog.views.searchblog', name='searchblog'),
	url(r'^blog/contact/', 'openshift.Blog.views.contact', name='contact'),
	url(r'^blog/contact2/', 'openshift.Blog.views.contact2', name='contact2'),
	url(r'^blog/contact3/', 'openshift.Blog.views.contact3', name='contact3'),
    # url(r'^openshift/', include('openshift.foo.urls')),
    #url(r'^posts/$', Blog.views.posts),
	#url(r'^contact/$', views.contact),
	#url(r'^i/$', views.i),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^blog/', include('Blog.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^blog/', include('Blog.urls')),
	#url(r'^about/', AboutView.as_view()),
	#url(r'^contact/$', views.contact),
	#url(r'^contact2/$', views.contact2),
	#url(r'^contact3/$', views.contact3),
    #url(r'^users/([\w-]+)/$', 'openshift.Blog.views.bookmark_list', name="bookmark_list"),
)
