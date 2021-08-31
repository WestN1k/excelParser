from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from apps.upload_files.constants import STATUS_PROCESSED, STATUS_COMPLETE
from apps.upload_files.models import UploadFile
from apps.upload_files.services import process_excel_file


@receiver(post_save, sender=UploadFile)
def processing_file(sender, instance, created, **kwargs):
    if created:
        instance.current_status = STATUS_PROCESSED
        instance.save()
        result = process_excel_file(instance.file)
        finish_date = now()
        instance.result = result
        instance.finish_date = finish_date
        instance.current_status = STATUS_COMPLETE
        instance.save()
