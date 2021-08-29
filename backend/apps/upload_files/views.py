from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.upload_files.models import UploadFile
from apps.upload_files.serializers import FileSerializer, FileUploadSerializer


class UploadViewSet(ReadOnlyModelViewSet):
    queryset = UploadFile.objects.all()
    parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        if self.action == 'upload':
            return FileUploadSerializer
        return FileSerializer

    @action(methods=['POST'], detail=False)
    def upload(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['file']:
            serializer.save()
            return Response({'file': 'has file'}, status=status.HTTP_200_OK)
        return Response({'file': 'no file'}, status=status.HTTP_204_NO_CONTENT)
