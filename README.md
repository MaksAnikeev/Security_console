# Пульт охранника банка

Проект написан на Django. 
Проект реализует следующие задачи:
- показывает список активных пропусков работника банка.
- показывает кто из работников сейчас в хранилище, время входа и сколько он там находится.
- показывает по каждому выбранному работнику перечень всех его визитов в хранилище, дату, их длительность и проверяет визиты на подозрительность.

Для работы программы необходимо SITE_SECRET_KEY(секретный код сайта), BD_PATH(адрес где находится база данных), BD_PASSWORD(пароль от базы данных). 
- Создать в корневом каталоге файл .env
- Записать в этом файле полученные `SITE_SECRET_KEY`, `BD_PATH`, `BD_PASSWORD`.
Для данного учебного проекта можно указать:
``` 
SECRET_KEY = 'REPLACE_ME'
BD_PATH = 'checkpoint.devman.org'
BD_PORT = '5434'
BD_NAME = 'checkpoint'
BD_USER = 'guard'
BD_PASSWORD = 'osim5'
DEBUG='True'
```

Чтобы запустить проект необходимо запустить файл `manage.py` и результат будет на сайте http://127.0.0.1:8000/
Пример запуска:
Заходите в папку с проектом где лежит файл `manage.py`
```
python manage.py bot runserver
```
В консоле выведет:
```
Performing system checks...

Watching for file changes with StatReloader
System check identified no issues (0 silenced).
August 15, 2022 - 06:21:22
Django version 3.2.15, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```


Описание и настройки вложенных файлов:

Файл `active_passcards_view` в папке `datacenter` фильтрует базу данных и выводит список только активных сотрудников банка, т.е. текущих работников банка.
Это настраивается здесь:
```py
active_passcards = Passcard.objects.filter(is_active=True)
```

Файл `storage_information_view` в папке `datacenter` определяет кто сейчас находится в хранилище и определяет подозрителен ли данный сотрудник.
Подозрительность определяется по времени нахождения в хранилище. Если более 60 минут, то подозрителен. Это настраивается здесь:
```py
is_strange = visitor.is_visit_long(start=visitor.entered_at,
                                           finish=current_time,
                                           minutes=60)
```

Файл `passcard_info_view` в папке `datacenter` выдает все визиты данного сотрудника в хранилище и определяет каждый визит на подозрительность.
Подозрительность определяется по времени нахождения в хранилище. Если более 60 минут, то подозрителен. Это настраивается здесь:
```py
is_strange = visit.is_visit_long(start=visit.entered_at,
                                         finish=visit.leaved_at,
                                         minutes=60)
```

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
