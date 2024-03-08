from django.urls import path, include

from petstagram.pets import views as v

urlpatterns = (
    path('add/', v.AddPetView.as_view(), name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', v.DetailsPetView.as_view(), name='details pet'),
        path('edit/', v.EditPetView.as_view(), name='edit pet'),
        path('delete/', v.DeletePetView.as_view(), name='delete pet'),
    ])),
)
