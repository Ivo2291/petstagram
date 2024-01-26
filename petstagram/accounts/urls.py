from django.urls import path, include

from petstagram.accounts import views as v

urlpatterns = (
    path('login/', v.login_user, name='login user'),
    path('register/', v.register_user, name='register user'),
    path('logout/', v.logout_user, name='logout user'),
    path('profile/<int:pk>/', include([
        path('', v.details_profile, name='details profile'),
        path('edit/', v.edit_profile, name='edit profile'),
        path('delete/', v.delete_profile, name='delete profile'),
    ])),
)
