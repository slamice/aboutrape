from django.conf.urls import patterns, include, url
from aboutrape.views import about, base, category
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', base),
    url(r'^/$', base),
	url(r'^about/$', about),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<category_id>\d+)/$', category, name='category'),
)