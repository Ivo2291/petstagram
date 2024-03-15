from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, views as auth_views
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm, ProfileEditForm
from petstagram.accounts.models import Profile


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

    return redirect('login user')


class DetailsProfileView(views.DetailView):
    queryset = Profile.objects.all() \
        .prefetch_related('user')

    template_name = 'accounts/details-profile.html'


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile.html'

    def get_success_url(self):
        return reverse('details profile', kwargs={
            'pk': self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['date_of_birth'].label = 'Birth Date'
        form.fields['date_of_birth'].type = 'Date'

        return form


def delete_profile(request, pk):
    context = {}

    return render(request, 'accounts/delete-profile.html', context)
