[![.github/workflows/main.yml](https://github.com/Denis-Galeev/kittygram_final/actions/workflows/main.yml/badge.svg)](https://github.com/Denis-Galeev/kittygram_final/actions/workflows/main.yml)

## Описание проекта

Проект для публикации фотографий котов и их достижений.

## Стек

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
- ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Для запуска проекта из образов с Docker hub

Cоздаём папку проекта `kittygram` и переходим в нее:

```bash
mkdir kittygram
cd kittygram
```

В папку проекта копируем (или создаём и заполняем) файл `docker-compose.production.yml` и запускаем его:

```bash
sudo docker compose -f docker-compose.production.yml up -d
```

Будут скачаны образы из dockerhub, на их основе поднимуться необходимые контейнеры, томы и сети.


## Для запуска проекта из исходников GitHub

Клонируем себе репозиторий: 

```bash 
git clone git@github.com:Denis-Galeev/kittygram_final.git
```

Выполняем запуск:

```bash
sudo docker compose -f docker-compose.yml up -d
```

## После запуска: Миграции, сбор статистики

После запуска нужно выполнить сбор статистики и миграцию для бэкенда. Статистика фронтенда собирается во время запуска контейнера, после чего он останавливается. 

```bash
sudo docker compose -f [имя-файла-docker-compose.yml] exec backend python manage.py migrate

sudo docker compose -f [имя-файла-docker-compose.yml] exec backend python manage.py collectstatic

sudo docker compose -f [имя-файла-docker-compose.yml] exec backend cp -r /app/collected_static/. /static/static/
```

теперь проект доступен на: 

```
http://localhost:9000/
```

## Описание переменных окружения

Ниже пример файла .env c переменными окружения, необходимыми для запуска приложения

```bash
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_NAME=kittygram
DB_HOST=db
DB_PORT=5432
DEBUG=False
SECRET_KEY=django_secret_key_example
ALLOWED_HOSTS=yoursite.example.com,localhost,127.0.0.1
USE_SQLITE=false
```


## Остановка оркестра контейнеров

В окне, где был запуск **Ctrl+С** или в другом окне:

```bash
sudo docker compose -f docker-compose.yml down
```

## Автор

Денис Галеев https://github.com/Denis-Galeev