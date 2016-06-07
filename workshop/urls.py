from django.conf.urls import patterns, include, url
from django.contrib import admin
from register.views import Home
from workshop.views import anonymous_required
from django.contrib.auth import views as auth_views
from register import urls as reg_url
urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'workshop.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('register.urls')),
    url(r'^user/login/$',
       anonymous_required(auth_views.login),
       {'template_name': 'login.html'},
       name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='logout'),

   )
