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

8100 - app, 8003 - phpmyadmin