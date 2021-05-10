from __future__ import print_function
import time
import os
import random

import cars_info_pb2
import cars_info_pb2_grpc
import grpc
from loguru import logger


logger.add('debug_client.log', format="{time},{level},{message}", level='DEBUG')

@logger.catch()
def get_one_model_info(stub, id):
    response = stub.GetInfoForModel(cars_info_pb2.RequestForOneModel(modelId=id))
    logger.info("Send request with id = {}", id)
    if response.info:
        for car in response.info:
            print("______Info______")
            print(f' Марка автомобиля: {car.brand}, модель автомобиля: {car.model}, '
                  f'год выпуска: {car.year} '
                  f'цена: {car.price}руб.')
    else:
        logger.warning("Model with this id was not found")
        print("Модель с таким id не найдена")

@logger.catch()
def get_info_for_brand(stub, id):

    for info in stub.GetInfoForBrand(cars_info_pb2.RequestForBrand(brandId=id)):
        print(f' Марка автомобиля: {info.brand}, модель автомобиля: {info.model}, '
              f'год выпуска: {info.year} '
              f'цена: {info.price}руб.')



@logger.catch()
def start(stub):
    while True:
        # 1
        user_answer = input("""
        Приветствуем Вас в нашем мини каталоге автомоболией!
        
        Выберите один из вариантов (ввести число): 
        1 - Получить информацию об автомобиле по id 
        2 - Получить информацию о рандомных 10 автомобилях
           
        3 - Получить информацию обо всех моделях марки выбранной марки.
         Чтобы выйти нажмите 'q'.
        
        """)
        if user_answer == "1":
            id_model = int(input("введите id модели"))
            get_one_model_info(stub, id_model)


        elif user_answer == "2":
            for x in range(1, 15):
                id = random.randint(1, 10)
                get_one_model_info(stub, id)
                print()
            time.sleep(10)

        elif user_answer == "3":
            get_info_for_brand(stub, 3)
            time.sleep(3)


        elif user_answer == "q":
            break



@logger.catch()
def run():
    HOST = os.getenv("HOST", "localhost")
    with grpc.insecure_channel(f"{HOST}:50051") as channel:
        stub = cars_info_pb2_grpc.InfoStub(channel)
        start(stub)



if __name__ == '__main__':
    run()
