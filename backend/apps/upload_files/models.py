from django.db import models

from apps.upload_files.constants import STATUS_CHOICES, STATUS_START
from apps.upload_files.validators import file_validate


class UploadFile(models.Model):
    upload_date = models.DateTimeField('Дата и время начала загрузки', auto_now_add=True)
    finish_date = models.DateTimeField('Дата и время окончания загрузки', null=True)
    current_status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=STATUS_START)
    result = models.CharField('результат обработки', blank=True, max_length=20)
    file = models.FileField('файл', upload_to='files/', validators=[file_validate])

    class Meta:
        verbose_name = 'Обработка файла'
        verbose_name_plural = 'Обработка файлов'
        ordering = ('-upload_date',)

    def __str__(self):
        return f'{self.file.name}, {self.finish_date}'
