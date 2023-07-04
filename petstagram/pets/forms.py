from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['slug']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),

            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'personal_pet_photo': forms.URLInput(
                attrs={'placeholder': 'Link to Image'}
            ),
        }

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_pet_photo': 'Link to Image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass
