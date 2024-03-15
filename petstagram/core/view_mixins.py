from django.contrib.auth import mixins as auth_mixins
from django.core import exceptions


class OwnerRequiredMixin(auth_mixins.LoginRequiredMixin):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        if obj.user != self.request.user:
            raise exceptions.PermissionDenied

        return obj
