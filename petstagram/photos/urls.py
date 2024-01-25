from django.urls import path, include

from petstagram.photos import views as v

urlpatterns = (
    path('add/', v.add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', v.details_photo, name='details photo'),
        path('edit/', v.edit_photo, name='edit photo')
    ])),
)
