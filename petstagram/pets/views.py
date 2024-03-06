from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            create_pet = form.save()

            return redirect('details pet', username='Ivo', pet_slug=create_pet.slug)

    context = {
        'form': form,
    }

    return render(request, 'pets/add-pet.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('details pet', username, pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet.slug,
    }

    return render(request, 'pets/edit-pet.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        form.save()

        return redirect('home page')

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet.slug,
    }

    return render(request, 'pets/delete-pet.html', context)


def details_pet(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }

    return render(request, 'pets/details-pet.html', context)
