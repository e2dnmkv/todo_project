## Как работать с проектом

1. Создать виртуальное окружение
```
python -m venv venv
```

2. Активировать его (macOS / Linux:)
```
source venv/bin/activate
```

3. Установить Django
```
pip install django
```

4. Применить миграции (создать/обновить таблицы в базе)
```
python manage.py migrate
```

5. Запустить сервер разработки
```
python manage.py runserver
```