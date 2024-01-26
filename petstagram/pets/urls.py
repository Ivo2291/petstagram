from django.urls import path, include

from petstagram.pets import views as v

urlpatterns = (
    path('add/', v.add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', v.details_pet, name='details pet'),
        path('edit/', v.edit_pet, name='edit pet'),
        path('delete/', v.delete_pet, name='delete pet'),
    ])),
)
