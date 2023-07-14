from django.db import models

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
        null=False
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ['date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
