from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(views.CreateView):
    form_class = PetCreateForm
    template_name = 'pets/add-pet.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': 'Ivo',
            'pet_slug': self.object.slug,
        })


class EditPetView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/edit-pet.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = 'Ivo'

        return context


class DeletePetView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/delete-pet.html'
    slug_url_kwarg = 'pet_slug'
    extra_context = {
        'username': 'Ivo',
    }
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs


class DetailsPetView(views.DetailView):
    queryset = Pet.objects.all()\
        .prefetch_related('photos')\
        .prefetch_related('photos__likes')\
        .prefetch_related('photos__tagged_pets')

    template_name = 'pets/details-pet.html'
    slug_url_kwarg = 'pet_slug'
