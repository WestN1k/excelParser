from django.apps import AppConfig


class UploadFilesConfig(AppConfig):
    name = 'apps.upload_files'

    def ready(self):
        from apps.upload_files import signals
