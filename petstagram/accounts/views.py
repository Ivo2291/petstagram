from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-user.html'
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-user.html'
    redirect_authenticated_user = True


def logout_user(request):
    logout(request)

    return redirect('home page')


def details_profile(request, pk):
    context = {}

    return render(request, 'accounts/details-profile.html', context)


def edit_profile(request, pk):
    context = {}

    return render(request, 'accounts/edit-profile.html', context)


def delete_profile(request, pk):
    context = {}

    return render(request, 'accounts/delete-profile.html', context)
