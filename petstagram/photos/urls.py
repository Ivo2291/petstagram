from django.urls import path, include

from petstagram.photos import views as v

urlpatterns = (
    path('add/', v.AddPhotoView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', v.DetailsPhotoView.as_view(), name='details photo'),
        path('edit/', v.EditPhotoView.as_view(), name='edit photo'),
        path('delete/', v.DeletePhotoView.as_view(), name='delete photo'),
    ])),
)
