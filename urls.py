from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'exlibris.views.home'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'base.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^register/', 'exlibris.views.register'),
    # url(r'^$', 'books.views.index')
)
