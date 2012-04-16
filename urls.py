from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
	url(r'(?i)^start_crawler\.json', 'crawler.views.start'),
	url(r'(?i)^new_crawler\.json', 'crawler.views.create'),
	url(r'(?i)^list\.json', 'crawler.views.list'),
	url(r'^/$', redirect_to, {'url': ''}),
	url(r'^$', 'web.views.ui'),


    # Examples:
    # url(r'^$', 'craigslist_apartments.views.home', name='home'),
    # url(r'^craigslist_apartments/', include('craigslist_apartments.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
