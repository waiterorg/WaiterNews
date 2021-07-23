from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from news_app.models import Article
from .forms import SignupForm
from .models import User
from .forms import ProfileForm
from .mixins import (FieldsMixin,
                     FormValidMixin,
                     AuthorAccessMixin,
                     SuperUserAccessMixin,
                     AuthorsAccessMixin,
                     )
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
# Create your views here.

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")

class ArticleList(AuthorsAccessMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = "registration/article-confirm-delete.html"


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm

    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class Register(CreateView):
    form_class = SignupForm
    template_name = "registration/register.html"
    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect(reverse('login'))
