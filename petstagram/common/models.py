from django.db import models

from petstagram.photos.models import Photo


class CommentPhoto(models.Model):
    COMMENT_MAX_LENGTH = 300

    text = models.CharField(
        max_length=COMMENT_MAX_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class LikePhoto(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
