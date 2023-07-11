from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


class Photo(models.Model):
    MAX_LENGTH_LOCATION = 30

    MAX_LENGTH_DESCRIPTION = 300
    MIN_LENGTH_DESCRIPTION = 10

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(
            validate_file_less_than_5mb,
        ),
        null=False,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=MAX_LENGTH_DESCRIPTION,
        validators=(
            MinLengthValidator(MIN_LENGTH_DESCRIPTION),
        ),
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
