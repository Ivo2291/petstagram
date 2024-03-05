from django.urls import path

from petstagram.common import views as v

urlpatterns = (
    path('', v.homepage, name='home page'),
    path('like_photo/<int:pk>/', v.likes_photo, name='likes photo'),
)
