WORKBOOK_COLUMNS = ['before', 'after']
FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'

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