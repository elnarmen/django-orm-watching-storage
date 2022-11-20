# Пульт охраны банка
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть,
как реализованны запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной БД с визитами и карточками сотрудников банка. Он отображает все активные карты доступа сотрудников банка, подробную информацию обо всех визитах в хранилище.

# Установка
Если у вас есть доступ к БД, вы можете запустить сайт у себя. Для этого следуйте инструкции по установке

## Переменные окружения
Создайте файл `.env` в директории проекта рядом с файлом `manage.py`.

Добавьте в файл `.env` переменные с необходимыми данными БД:
```
ENGINE 
HOST 
PORT 
NAME 
USER 
PASSWORD 
SECRET_KEY
DEBUG=True
```
На вашем компьютере уже должен быть установлен Python3. Для загрузки проекта откройте терминал и перейдите в папку, в которую хотите загрузить файлы.

Затем введите команду:
```
git clone https://github.com/elnarmen/django-orm-watching-storage.git
```
## Настройка виртуального окружения
Перейдите в папку с проектом:
```
cd django-orm-watching-storage
```
Далее введите команду:
```
python -m venv venv
```
Активируйте виртуальное окружение командой:
```
cd venv\Scripts
activate.bat
```
Затем вернитесь в папку с проектом:
```
cd ../..
```
## Установка зависимостей
Используйте pip для установки зависимостей:

   ```
   pip install -r requirements.txt
   ```

## Запуск
Для того, чтобы запустить сайт, перейдите в директорию с файлом `manage.py` и введите команду:
```
python manage.py runserver
```
Cайт будет запущен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
# Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
