from django.db import models
from django.db.models import ForeignKey

from petstagram.photos.models import Photo


class Comment(models.Model):
    MAX_COMMENT_LENGTH = 300

    comment_text = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
