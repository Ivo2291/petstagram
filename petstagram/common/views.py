from django.shortcuts import redirect

from petstagram.common.models import LikePhoto

from django.views import generic as views

from petstagram.photos.models import Photo


# def homepage(request):
#     pet_name_pattern = request.GET.get('pet_name_pattern', None)
#
#     pet_photos = Photo.objects.all()
#
#     if pet_name_pattern:
#         pet_photos = pet_photos.filter(tagged_pets__name__icontains=pet_name_pattern)
#
#     context = {
#         'pet_photos': pet_photos,
#         'pet_name_pattern': pet_name_pattern,
#     }
#
#     return render(request, 'common/home-page.html', context)


class HomePageView(views.ListView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('likes')

    template_name = 'common/home-page.html'
    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query['tagged_pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)


def likes_photo(request, pk):
    pet_photo_like = LikePhoto.objects.filter(to_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        LikePhoto.objects.create(to_photo_id=pk)

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')
