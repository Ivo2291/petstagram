from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet


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
    pet = Pet.objects.filter(slug=pet_slug).get()

    form = PetEditForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('details pet', username, pet_slug)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def details_pet(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
