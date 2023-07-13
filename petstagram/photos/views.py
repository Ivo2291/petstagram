from django.shortcuts import render, redirect

from petstagram.common.utils import get_user_liked_photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}

    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    form = PhotoEditForm(request.POST or None, instance=photo)

    if form.is_valid():
        form.save()
        return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    context = {
        'photo': photo,
        'user_liked_photo': get_user_liked_photo(pk),
        'likes_count': photo.like_set.count(),
    }

    return render(request, 'photos/photo-details-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()

    return redirect('index')
