# Generated by Django 3.2.19 on 2023-06-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.Pet'),
        ),
    ]
