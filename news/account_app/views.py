from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        return reverse_lazy("news:articlelist")
