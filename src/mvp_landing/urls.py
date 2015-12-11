from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/', 'signups.views.portfolio'),
    url(r'^enquire/', 'signups.views.enquire'),
    #(r'^pages/', include('django.contrib.flatpages.urls')),
    # url(r'^blog/', include('blog.urls')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
		  document_root=settings.MEDIA_ROOT)
