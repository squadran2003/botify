from django import template
from django.db.models import FileField

register = template.Library()


@register.filter
def is_file_field(field):
    return isinstance(field.field, FileField)