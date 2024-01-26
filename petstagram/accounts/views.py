from django.shortcuts import render, redirect


def register_user(request):
    context = {}

    return render(request, 'accounts/register-user.html', context)


def login_user(request):
    context = {}

    return render(request, 'accounts/login-user.html', context)


def logout_user(request):
    return redirect('home page')


def details_profile(request, pk):
    context = {}

    return render(request, 'accounts/details-profile.html', context)


def edit_profile(request, pk):
    context = {}

    return render(request, 'accounts/edit-profile.html', context)


def delete_profile(request, pk):
    context = {}

    return render(request, 'accounts/delete-profile.html', context)
