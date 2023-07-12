from petstagram.common.models import Like


def get_user_liked_photo(photo_id):
    # TODO: fix when auth is learned

    return Like.objects.filter(photo_id=photo_id)


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
