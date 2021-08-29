from django.db import models

from apps.upload_files.validators import file_validate


class UploadFile(models.Model):
    STATUS_START = 'start'
    STATUS_PROCESSED = 'processed'
    STATUS_COMPLETE = 'complete'
    STATUS_ERROR = 'error'

    STATUS_CHOICES = (
        (STATUS_START, 'Начало загрузки'),
        (STATUS_PROCESSED, 'Обработка'),
        (STATUS_COMPLETE, 'Обработан'),
        (STATUS_ERROR, 'Ошибка'),
    )

    upload_date = models.DateTimeField('Дата и время начала загрузки', auto_now_add=True)
    finish_date = models.DateTimeField('Дата и время окончания загрузки', blank=True)
    current_status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=STATUS_START)
    result = models.CharField('результат обработки', blank=True, max_length=20)
    file = models.FileField('файл', upload_to='files/', validators=[file_validate])

    class Meta:
        verbose_name = 'Обработка файла'
        verbose_name_plural = 'Обработка файлов'
        ordering = ('-upload_date',)

    def __str__(self):
        return f'{self.file.name}, {self.finish_date}'
