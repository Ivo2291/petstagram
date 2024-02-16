from django.shortcuts import render

from petstagram.photos.models import Photo


def homepage(request):
    context = {
        'pet_photos': Photo.objects.all(),
    }

    return render(request, 'common/home-page.html', context)
