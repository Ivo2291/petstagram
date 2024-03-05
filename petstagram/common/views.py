from django.shortcuts import render, redirect

from petstagram.common.models import LikePhoto
from petstagram.photos.models import Photo


def homepage(request):
    context = {
        'pet_photos': Photo.objects.all(),
    }

    return render(request, 'common/home-page.html', context)


def likes_photo(request, pk):
    pet_photo_like = LikePhoto.objects.filter(to_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        LikePhoto.objects.create(to_photo_id=pk)

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')
