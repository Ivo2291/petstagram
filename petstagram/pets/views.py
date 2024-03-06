from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetCreateView(views.CreateView):
    form_class = PetCreateForm
    template_name = 'pets/add-pet.html'

    def get_success_url(self):
        return reverse_lazy('details pet', kwargs={
            'username': 'Ivo',
            'pet_slug': self.object.slug,
        })


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/edit-pet.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy('details pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = 'Ivo'

        return context


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        form.save()

        return redirect('home page')

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet.slug,
    }

    return render(request, 'pets/delete-pet.html', context)


class PetDetailsView(views.DetailView):
    model = Pet
    template_name = 'pets/details-pet.html'
    slug_url_kwarg = 'pet_slug'
