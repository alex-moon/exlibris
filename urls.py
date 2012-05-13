from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'base.html'}),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

urlpatterns += patterns('books.views',
    url(r'^register', 'register'),
    url(r'^dashboard', 'dashboard'),
    url(r'^text/(?P<slug>[-a-z0-9]+)', 'text'),
    url(r'^books/add', 'addBook'),
    url(r'^json/(?P<model>[a-zA-Z]+)/(?P<field>[a-zA-Z]+)', 'ajaxSearch'),
    url(r'^$', 'home'),
)
