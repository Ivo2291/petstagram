from django.core.exceptions import ValidationError


def validate_file_size(file_obj):
    if file_obj.size > 5242880:
        raise ValidationError('The file size should not be above 5MB!')
