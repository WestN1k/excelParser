## Обработчик Excel файлов

### Используемые фреймворки
- Django 3
- Django Rest Framework 3

В качестве менеджера зависимостей используется Poetry.


## Запуск проекта

Требуется создать и поместить в корень проекта **.env** файл с данными:

    DEBUG=True
    SECRET_KEY='django-somekey'
    DB_NAME='postgres'
    DB_USER='postgres'
    DB_PASSWORD='postgres'
    SUPERUSER_NAME='qwerty'
    SUPERUSER_EMAIL='qwerty@mail.ru'
    SUPERUSER_PASSWORD='qwerty123'

Запуск контейнеров осуществляется через команду из корня проекта:

`docker-compose up -d --build`

Далее API доступно через **localhost**

## Авторизация
Установлена стандартная авторизация DRF. 

При первом запуске контейнеров в БД создается супер пользователь:  
**Логин:** qwerty  
**Пароль:** qwerty123

\* можно поменять данные суперпользователя через .env файл

Для доступа к API достаточно зайти в [http://localhost/admin](http://localhost/admin)



## Адреса
[http://localhost/api/file/](http://localhost/api/file/) - Список файлов  
[http://localhost/api/file/upload](http://localhost/api/file/upload) - Загрузка файла
