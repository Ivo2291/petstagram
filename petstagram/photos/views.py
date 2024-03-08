from django.urls import reverse, reverse_lazy

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo

from django.views import generic as views


class AddPhotoView(views.CreateView):
    Model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/add-photo.html'

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk
        })


class EditPhotoView(views.UpdateView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes') \
        .prefetch_related('comments')

    form_class = PhotoEditForm
    template_name = 'photos/edit-photo.html'

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk
        })


class DeletePhotoView(views.DeleteView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes') \
        .prefetch_related('comments')

    template_name = 'photos/delete-photo.html'
    success_url = reverse_lazy('home page')


class DetailsPhotoView(views.DetailView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes') \
        .prefetch_related('comments')

    template_name = 'photos/details-photo.html'
