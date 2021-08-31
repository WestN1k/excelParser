import os
from django.db import migrations
from django.contrib.auth.models import User


class Migration(migrations.Migration):
    dependencies = [
        ('upload_files', '0001_initial'),
    ]

    def generate_superuser(self, schema_editor):
        SUPERUSER_NAME = os.environ.get('SUPERUSER_NAME')
        SUPERUSER_EMAIL = os.environ.get('SUPERUSER_EMAIL')
        SUPERUSER_PASSWORD = os.environ.get('SUPERUSER_PASSWORD')

        superuser = User.objects.create_superuser(
            username=SUPERUSER_NAME, email=SUPERUSER_EMAIL, password=SUPERUSER_PASSWORD
        )
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
