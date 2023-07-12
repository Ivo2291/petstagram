def apply_likes_count_photo(photo):
    photo.likes_count = photo.like_set.count()

    return photo


def apply_user_liked_photo(photo):
    # TODO: fix it for current user when authentication is learned
    photo.is_liked = photo.likes_count > 0

    return photo
