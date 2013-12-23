from django.conf.urls import patterns, url

urlpatterns = patterns(
    'usuarios.views',
    url(r'^registra/$', 'registra', name='registra'),
    url(r'^escritorio/$', 'escritorio', name='escritorio'),
    url(r'^logout/$', 'logouts', name='logouts'),
    url(r'^add_key/$', 'add_key', name='add_key'),
    url(r'^edit_key/$', 'edit_key', name='edit_key'),
    url(r'^delete_key/$', 'delete_key', name='delete_key'),
)
