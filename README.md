Тестовое задания по созданию API и взаимодейстие со API stripe


Для запуска сайта необходимо заполнить переменные окружения
в docker-compose и в файле .env.

Следующие переменные в docker-compose ставим в сервис stripe_payment:

`DJANGO_SECRET_KEY` — ключ безопасности django.

`PAYMENT_HOST` — имя хоста для вашей БД. При запуске через docker-compose надо установить значение 'db' и в 
docker-compose, и в файле .env, если запускаем без него ставим localhost в .env.

`PAYMENT_PASSWORD` — пароль пользователя привязанного к БД.

`PAYMENT_PORT` — порт для подключения к ДБ (по дефолту 5432).

`PAYMENT_USER` — пользователь привязанный к БД.

`PAYMENT_NAME` — имя вашей БД.

`STRIPE_PUBLIC_KEY` — публичный ключ stripe.

`STRIPE_SECRET_KEY` - секретный ключ stripe.

Следующие переменные в docker-compose ставим в сервис db:

`POSTGRES_PASSWORD` - пароль пользователя привязанного к БД.

`POSTGRES_USER` - пользователь привязанный к БД.

`POSTGRES_DB` - имя вашей БД.

Далее выполняем по порядку следущющие команды:

`docker-compose build`
`docker-compose up`

Далее открываем второе окно терминала для создания супер пользователя:

`docker exec -it stripe_payment python manage.py createsuperuser`

После создания суперпользователя переходим по открытому докером адресу `http://0.0.0.0:8000/`, но там не будет
отображаться наша страница, чтобы её увидеть нужно перейти на адрес `http://localhost:8000/`, Далее в админке django 
создать тестовые объекты в базе данных (если их нет) и протестировать API.

!!! В поле ЦЕНА нужно добавлять не менее 5000 иначе API stripe выдаст ошибку !!!







