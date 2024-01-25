from django.shortcuts import render


def homepage(request):
    context = {}

    return render(request, 'common/home-page.html', context)
