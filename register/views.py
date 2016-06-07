from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from register.forms import *


class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj

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

class chocolate_detailview(ListView):
    template_name= "chocolate_detail.html"

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

class ChocolateDetailsView(DetailView):
    template_name = "chocolate_detail.html"

    def get_object(self, queryset=None):
        choco_id = self.kwargs['choco_id']
        obj = Chocolate.objects.get(id=choco_id)
        if obj:
            return obj
        else:
            raise Http404("No details Found.")


class UserProfileUpdateView(LoginRequiredMixin, CurrentUserMixin, UpdateView):
    model = User
    fields = user_fields + user_extra_fields
    template_name = 'edit_profile.html'
    success_url = '/register/user/profile/'


