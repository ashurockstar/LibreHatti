from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

next_page = reverse_lazy('librehatti.catalog.views.index')


urlpatterns = patterns('',
        (r'^login$', 'django.contrib.auth.views.login', 
        {'template_name': 'userAccounts/login.html'}),
        (r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 
        next_page}),
        (r'^signup$', 'useraccounts.views.register'),
)

