from django.contrib import admin

from petstagram.common.models import CommentPhoto, LikePhoto


@admin.register(CommentPhoto)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )


@admin.register(LikePhoto)
class LikeAdmin(admin.ModelAdmin):
    pass
