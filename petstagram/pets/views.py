from django.shortcuts import render


def add_pet(request):
    context = {}

    return render(request, 'pets/add-pet.html', context)


def details_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/details-pet.html', context)


def edit_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/edit-pet.html', context)


def delete_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/delete-pet.html', context)
