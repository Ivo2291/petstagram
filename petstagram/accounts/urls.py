from django.urls import path, include

from petstagram.accounts import views as v

urlpatterns = (
    path('signup/', v.signup_user, name='signup user'),
    path('signin/', v.signin_user, name='signin user'),
    path('profile/<int:pk>/', include([
        path('', v.details_profile, name='details profile'),
        path('edit/', v.edit_profile, name='edit profile'),
        path('delete/', v.delete_profile, name='delete profile'),
    ])),
)
