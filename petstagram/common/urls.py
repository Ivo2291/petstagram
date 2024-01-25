from django.urls import path

from petstagram.common import views as v

urlpatterns = (
    path('', v.homepage, name='home page'),
)
