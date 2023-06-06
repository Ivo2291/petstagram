from django.urls import path, include
from petstagram.accounts import views

urlpatterns = (
    path('register/', views.register_account, name='register account'),
    path('login/', views.login_account, name='login account'),
    path('profile/<int:pk>/', include([
        path('', views.details_account, name='details account'),
        path('edit/', views.edit_account, name='edit account'),
        path('delete/', views.delete_account, name='delete account'),
        ]
    ))
)
