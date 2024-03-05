from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    context = {}

    return render(request, 'photos/add-photo.html', context)


def edit_photo(request, pk):
    context = {}

    return render(request, 'photos/edit-photo.html', context)


def details_photo(request, pk):
    context = {
        'pet_photo': Photo.objects.get(pk=pk)
    }

    return render(request, 'photos/details-photo.html', context)
