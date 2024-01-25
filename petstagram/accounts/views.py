from django.shortcuts import render


def signin_user(request):
    context = {}

    return render(request, 'accounts/signin-user.html', context)


def signup_user(request):
    context = {}

    return render(request, 'accounts/signup-user.html', context)


def details_profile(request, pk):
    context = {}

    return render(request, 'accounts/details-profile.html', context)


def edit_profile(request, pk):
    context = {}

    return render(request, 'accounts/edit-profile.html', context)


def delete_profile(request, pk):
    context = {}

    return render(request, 'accounts/delete-profile.html', context)
