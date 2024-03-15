from django.contrib.auth import get_user_model, forms as auth_forms

UserModel = get_user_model()


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)


class PetstagramUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = ('email',)
