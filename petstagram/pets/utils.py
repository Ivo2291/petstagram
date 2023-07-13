from petstagram.pets.models import Pet


def get_pet_by_slug_and_username(username, pet_slug):
    # TODO: fix username when auth is learned

    return Pet.objects.get(pet_slug=pet_slug)
