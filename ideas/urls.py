from django.conf.urls import patterns, include, url
from webapp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ideas.views.home', name='home'),
    # url(r'^ideas/', include('ideas.foo.urls')),
    url(r'^$', include('webapp.urls', namespace="webapp")),
    url(r'^webapp/', include('webapp.urls', namespace="webapp")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
