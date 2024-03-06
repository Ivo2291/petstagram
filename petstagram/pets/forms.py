from django import forms

from petstagram.core.form_mixins import ReadonlyFieldsFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'pet_photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'pet_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'name': 'Pet name',
            'pet_photo': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(ReadonlyFieldsFormMixin, PetBaseForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
