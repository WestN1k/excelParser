from django.contrib.admin import register, ModelAdmin

from apps.upload_files.models import UploadFile


@register(UploadFile)
class UploadFileAdmin(ModelAdmin):
    pass
