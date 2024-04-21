# Anverali-Test
## Task
Необходимо создать сайт с админ панелью и 2-мя кабинетами на Flask или Django. Сайт может быть не оформлен красиво. Структура на выбор. Можно взять за основу сайт kwork.ru. На сайте помимо админки должны быть два кабинета заказчика и исполнителя. Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL

## For start
### Create .env and set:
```
DEBUG=TRUE
SECRET_KEY=SECRET_KEY
ALLOWED_HOSTS=localhost

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=strong_password
```

### Start:
```
docker-compose.yml up
```

###  After start in docker: make migration and create superuser
