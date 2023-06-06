from django.shortcuts import render


def register_account(request):
    return render(request, 'accounts/register-page.html')


def login_account(request):
    return render(request, 'accounts/login-page.html')


def details_account(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_account(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_account(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
