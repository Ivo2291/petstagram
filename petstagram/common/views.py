from django.shortcuts import render

from petstagram.photos.models import Photo


def apply_likes_count_photos(photo):
    photo.likes_count = photo.like_set.count()

    return photo


def apply_user_liked_photos(photo):
    # TODO: fix it for current user when authentication is learned
    photo.is_liked = photo.likes_count > 0

    return photo


def index(request):
    photos = [apply_likes_count_photos(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photos(photo) for photo in photos]

    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)
