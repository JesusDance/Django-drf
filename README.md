# Djngo-drf


## Description
An app with complex integration with standard forms
and drf plus the app using jwt token.


## Features
- create, update, delete users profile and their games too
- authentication
- unittests
- PostgreSQL


## TechStack
- Django
- Django DRF
- PyJWT
- whitenoise
- drf-yasg (OpenAPI specification as swagger)
- PostgreSQL
- Bootstrap
- Unittests
- Docker (Dockerfile, Docker compose)
- Black (for PIP8)
- .env file
- Deploy using Render https://django-drf-1k5v.onrender.com
- Neon database for cloud host


## Instalation
1. Clone repo
git clone https://github.com/JesusDance/Django-drf
cd Django_drf/django_start

2. Create virtual environment
python3 -m venv venv
source .venv/bin/activate #Linux/Mac
.venv/Scripts/activate    # Windows

3. Install dependencies
python install -r requirements.txt

4. SSL turn off
django_start/settings.py/SECURE_SSL_REDIRECT = False

5. Run app
python manage.py runserver

App runs at
http://127.0.0.1:8000


# Endpoints

## OpenAPI swagger
http://127.0.0.1:8000/api/docs/

## django_db
http://127.0.0.1:8000/admin/ POST (superuser)
http://127.0.0.1:8000/ POST (create user)
http://127.0.0.1:8000/login/ POST
http://127.0.0.1:8000/logout/ POST
http://127.0.0.1:8000/update/ PATCH (update users profile)
http://127.0.0.1:8000/delete/ DELETE (delete user with games)
http://127.0.0.1:8000/accounts/profile/ POST (create profile)

http://127.0.0.1:8000/client/game/ POST (create game)
http://127.0.0.1:8000/get-game/<int:game_id>/ GET
http://127.0.0.1:8000/get-gamelist/ GET
http://127.0.0.1:8000/game-update/<int:game_id>/ PATCH
http://127.0.0.1:8000/game-delete/<int:game_id>/ DELETE

## django_api
http://127.0.0.1:8000/create-user/ POST (create-user)
http://127.0.0.1:8000/games/ GET, POST
http://127.0.0.1:8000/games/<int:game_id>/ POST, GET, PUT, PATCH, DELETE
http://127.0.0.1:8000/api-auth/login/ POST

## drf_jwt
http://127.0.0.1:8000/register/ POST
http://127.0.0.1:8000/register/profile/ GET
http://127.0.0.1:8000/api/auth/login/ POST
http://127.0.0.1:8000/api/auth/refresh/ POST
