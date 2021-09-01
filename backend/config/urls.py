from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.upload_files.urls import file_router


router = DefaultRouter()

router.registry.extend(file_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
