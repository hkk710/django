from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from register.forms import *


class Home(TemplateView):
    template_name="index.html"

    def get_queryset(self):
        return Chocolate.object.all()

class profileView(TemplateView):
    template_name="profile.html"

    def get_queryset(self):
        return Chocolate.object.all()


class chocolatelistview(ListView):
    template_name="list.html"

    def get_queryset(self):
        return Chocolate.objects.all()



class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = reverse_lazy(u"home")
  #  success_url = '/register/user/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class AddchocolateView(FormView):
    template_name = "add_chocolate.html"
    form_class = ChocolateAddForm
    success_url = '/register/chocolate/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

