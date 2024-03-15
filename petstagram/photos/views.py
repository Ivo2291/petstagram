from django.urls import reverse, reverse_lazy

from petstagram.core.view_mixins import OwnerRequiredMixin
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo

from django.views import generic as views


class AddPhotoView(OwnerRequiredMixin, views.CreateView):
    Model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/add-photo.html'

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


class EditPhotoView(OwnerRequiredMixin,  views.UpdateView):
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


class DeletePhotoView(OwnerRequiredMixin, views.DeleteView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes') \
        .prefetch_related('comments')

    template_name = 'photos/delete-photo.html'
    success_url = reverse_lazy('home page')


class DetailsPhotoView(OwnerRequiredMixin, views.DetailView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes') \
        .prefetch_related('comments')

    template_name = 'photos/details-photo.html'
