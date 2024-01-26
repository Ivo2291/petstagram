from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=[
            validate_file_size,
        ],
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )
