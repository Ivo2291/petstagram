from django import forms

from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']

        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['photo']

        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }
