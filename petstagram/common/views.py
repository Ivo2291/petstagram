import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.forms import CommentForm
from petstagram.common.models import Like
from petstagram.common.utils import get_user_liked_photo, get_photo_url
from petstagram.core.photo_utils import apply_likes_count_photo, apply_user_liked_photo
from petstagram.photos.models import Photo


def index(request):
    photos = [apply_likes_count_photo(photo) for photo in Photo.objects.all().order_by('pk')]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    comment_form = CommentForm()

    context = {
        'photos': photos,
        'comment_form': comment_form,
    }

    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photo = get_user_liked_photo(photo_id)

    if not user_liked_photo:
        Like.objects.create(
            to_photo_id=photo_id,
        )
    else:
        user_liked_photo.delete()

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)

    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()

    return redirect(get_photo_url(request, photo_id))
