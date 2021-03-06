from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'incubu.views.home', name='home'),
    # url(r'^incubu/', include('incubu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^control/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^usuario/', include('usuarios.urls')),
    url(r'^acerca/$', TemplateView.as_view(template_name='home/acercade.html')),
)
