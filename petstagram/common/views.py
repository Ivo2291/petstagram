from django.shortcuts import render, redirect

from petstagram.common.models import LikePhoto
from petstagram.photos.models import Photo


def homepage(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)

    pet_photos = Photo.objects.all()

    if pet_name_pattern:
        pet_photos = pet_photos.filter(tagged_pets__name__icontains=pet_name_pattern)

    context = {
        'pet_photos': pet_photos,
        'pet_name_pattern': pet_name_pattern,
    }

    return render(request, 'common/home-page.html', context)


def likes_photo(request, pk):
    pet_photo_like = LikePhoto.objects.filter(to_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        LikePhoto.objects.create(to_photo_id=pk)

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')
