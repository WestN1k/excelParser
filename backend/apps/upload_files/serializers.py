from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, FileField

from apps.upload_files.models import UploadFile
from apps.upload_files.services import format_datetime
from apps.upload_files.validators import file_validate


class FileSerializer(ModelSerializer):
    upload_date = SerializerMethodField()
    finish_date = SerializerMethodField()

    class Meta:
        model = UploadFile
        fields = ('upload_date', 'finish_date', 'result', 'current_status')

    @staticmethod
    def get_upload_date(obj):
        return format_datetime(obj.upload_date)

    @staticmethod
    def get_finish_date(obj):
        return format_datetime(obj.finish_date)


class FileUploadSerializer(ModelSerializer):
    file = FileField(validators=[file_validate])

    class Meta:
        model = UploadFile
        fields = ('file',)
