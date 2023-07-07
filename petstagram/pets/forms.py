from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['pet_slug']

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


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.disabled = True
            field.widget.attrs['readonly'] = 'readonly'
