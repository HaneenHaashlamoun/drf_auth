# drf_auth
https://github.com/HaneenHaashlamoun/drf_auth/pulls/1

## Feature Tasks and Requirements
### Features - Django
- [x] Add JWT Authentication to your API.
    - [x] Install needed libraries in project configuration and/or site settings.
- [x] Keep any pre-existing authentication so DRF Browsable API still usable.
    - [x] Install needed libraries in project configuration and/or site settings.

### Features - Docker
- [x] Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.
    - [x] E.g. as a VS Code snippet, or a gist.
- [x] Switch to using Gunicorn instead of Django’s built in development server.
    - [x] mind the number of workers to avoid sluggishness
- [x] Warning You will run into styling issues when you switch over to Gunicorn.
    - [x] On Django side you’ll need to properly handle static files using Whitenoise

### Storage Options
- [x] Your choice of SQLite or PostgreSQL
- [x] Adjust docker-compose.yml so that data is persisted in a volume outside of container.
    - [x] These steps are different depending on whether SQLite or PostgreSQL is being used.

    