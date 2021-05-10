# test_grpc_progect

Старт

1) Создать образ 

docker-compose build

2) Запустить контейнер с базой в терминале 

  docker-compose up bd

3) Запустить контейнер с сервером

docker-compose up server

4) Запустить  в контейнере serve файл db_init.py для созданияданных в базе.

docker-compose exeс server python db_init.py

5) Запустить контейнер с клиентом

docker-compose up client
