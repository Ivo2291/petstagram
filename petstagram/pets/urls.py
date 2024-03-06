from django.urls import path, include

from petstagram.pets import views as v

urlpatterns = (
    path('add/', v.PetCreateView.as_view(), name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', v.PetDetailsView.as_view(), name='details pet'),
        path('edit/', v.PetEditView.as_view(), name='edit pet'),
        path('delete/', v.delete_pet, name='delete pet'),
    ])),
)
