from django.utils.timezone import now
from rest_framework.serializers import ModelSerializer, FileField

from apps.upload_files.models import UploadFile
from apps.upload_files.services import process_excel_file
from apps.upload_files.validators import file_validate


class FileSerializer(ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('upload_date', 'finish_date', 'result', 'current_status')


class FileUploadSerializer(ModelSerializer):
    file = FileField(validators=[file_validate])

    class Meta:
        model = UploadFile
        fields = ('file',)

    def create(self, validated_data):
        file = validated_data['file']
        result = process_excel_file(file)
        finish_date = now()
        return UploadFile.objects.create(result=result, finish_date=finish_date, **validated_data)
