from rest_framework.routers import DefaultRouter

from apps.upload_files.views import UploadViewSet


file_router = DefaultRouter()

file_router.register(r'file', UploadViewSet, basename='upload_file')
