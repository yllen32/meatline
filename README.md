# meetline
Интернет магазин для мясной лавки

![4ruz8jHqEW](https://user-images.githubusercontent.com/104005279/193827664-5b9db2b7-6304-4087-a950-0f93b3b175a3.gif)

## Реализованные Особенности

*Отсутсвие регистрации для пользователей

*Хранение данных о корзине и покупках за счёт куки файлов. 

# Установка

Убедитесь что у вас установлен python версии 3.8 как минимум

Создайте директории для проекта на и сделайте git clone:

    $ git clone https://github.com/yllen32/meetline
    
Установите виртуальное окружение и активируйте его:
    
    $ python -m venv venv
    $ source venv/Scrits/Activate

Установите все необходимые зависимости:
    
    $ pip install -r requirements.txt

Создайте свой файл локальной переменной для хранения конфедициальной информации (SECRET_KEY DEBAG_STATUS)
Смотрите .env template для для примера

SECRET KEY вы можете сгенерировать с помощью команд


    from django.core.management.utils import get_random_secret_key  
    get_random_secret_key()

Вы можете запустить сервер разработчика:

    $ python manage.py runserver

Для связи с автором, вы можете написать на почту:
    furtov1995@yandex.ru
