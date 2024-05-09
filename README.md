# MFSO

This app tested on ubuntu 20.04, python 3.10, sqllite3

To run this app:
+ install python3, pip3, python3-venv
+ copy this project 
+ cd project/dj
+ python3 -m venv venv
+ source venv/bin/activate (activate virtual enviroment)
+ pip3 install -r requirements.txt (install dependencies)
+ ./manage.py migrate (apply migrations for DB, if you need)
+ ./manage.py loaddata fixture/department.json (if you run at first)
+ ./manage.py loaddata fixture/imns.json (if you run at first)
+ ./manage.py loaddata fixture/user.json (if you run at first)
+ ./manage.py runsever {ip:port} (start app)


To run in Docker-compose
docker-compose up

8100 - app, 8003 - phpmyadmin