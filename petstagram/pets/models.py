from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_LENGTH_NAME = 30

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    personal_pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    pet_slug = models.SlugField(
        unique=True,
        editable=False,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.pet_slug:
            self.pet_slug = slugify(f"{self.id}-{self.name}")

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Name={self.name} - ID={self.id}"
