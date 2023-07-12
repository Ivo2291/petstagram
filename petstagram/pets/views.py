from django.shortcuts import render, redirect

from petstagram.core.photo_utils import apply_likes_count_photo, apply_user_liked_photo
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.utils import get_pet_by_slug_and_username


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('details account', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    # TODO: set user when auth is learned

    pet = get_pet_by_slug_and_username(username, pet_slug)

    form = PetEditForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def details_pet(request, username, pet_slug):
    pet = get_pet_by_slug_and_username(username, pet_slug)
    photos = [apply_likes_count_photo(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'total_photos': pet.photo_set.count(),
        'photos': photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def delete_pet(request, username, pet_slug):
    # TODO: set user when auth is learned

    pet = get_pet_by_slug_and_username(username, pet_slug)

    form = PetDeleteForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('details account', pk=1)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }
    return render(request, 'pets/pet-delete-page.html', context)
