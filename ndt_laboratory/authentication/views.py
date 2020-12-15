from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views


class SignUpView(views.CreateView):
    pass


class SignInView(auth_views.LoginView):
    template_name = 'auth/signin.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')

