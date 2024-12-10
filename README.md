# MFSO

This app tested on ubuntu 20.04, docker

To run this app:
+ install docker
+ copy this project 
+ cd MSFO
+ docker compose build
+ docker compose up

For create migrations: 
+ docker compose run --rm web python manage.py makemigrations

For python console:
+ docker compose up -d
+ docker compose exec web python manage.py shell



8100 - app, 8003 - phpmyadmin