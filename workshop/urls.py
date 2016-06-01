from django.conf.urls import patterns, include, url
from django.contrib import admin
from register.views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),


)
