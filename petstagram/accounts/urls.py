from django.urls import path, include

from petstagram.accounts import views as v

urlpatterns = (
    path('login/', v.LoginUserView.as_view(), name='login user'),
    path('register/', v.RegisterUserView.as_view(), name='register user'),
    path('logout/', v.logout_user, name='logout user'),
    path('profile/<int:pk>/', include([
        path('', v.DetailsProfileView.as_view(), name='details profile'),
        path('edit/', v.EditProfileView.as_view(), name='edit profile'),
        path('delete/', v.delete_profile, name='delete profile'),
    ])),
)
