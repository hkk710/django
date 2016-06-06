from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from register import views
from register.views import *
from register.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='sucess.html'),    name='page'),
    url(r'^chocolate/add', AddchocolateView.as_view(), name= "add_chocolate"),
    url(r'^chocolate/list', chocolatelistview.as_view(), name= "list"),
    url(r'^user/profile', profileView.as_view(), name= "profile")
]