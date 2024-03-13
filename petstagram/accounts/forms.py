from django.contrib.auth import forms as auth_forms

from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = PetstagramUser
        fields = ("email",)
