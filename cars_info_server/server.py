import os
from concurrent import futures

import cars_info_pb2_grpc
import grpc
import psycopg2
import psycopg2.extras
from cars_info_pb2 import InfoForOneModel, ResponseForOneModel, ResponseInfoForBrand,InfoForOneModel
from loguru import logger

logger.add('debug_server.log', format="{time},{level},{message}", level='DEBUG')

DB_USER = "postgres"
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "test")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_PASSWORD = os.getenv("DB_PASSWORD", 'admin')

@logger.catch()
def select_data(id):
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cur = connection.cursor()

        insert_query_to_select = """
        select  b.brand_name, m.model, m.year, p.price
        from brands b
        join models m on b.id = m.brandId
        join price p on m.id = p.modelId
        where m.id = %s
        """

        model_id = (id,)
        logger.info('select_query {} with id {}', insert_query_to_select, model_id)
        cur.execute(insert_query_to_select, model_id)
        info = cur.fetchone()
        # logger.debug('response from db = {}', info)
        return info

    except (Exception, psycopg2.Error) as error:
        if (connection):
            logger.error("Error {}", error)

    finally:
        if (connection):
            cur.close()
            connection.close()

@logger.catch()
def select_brand(id):
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cur = connection.cursor()

        insert_query_to_select = """
        select  b.brand_name, m.model, m.year, p.price
        from brands b
        join models m on b.id = m.brandId
        join price p on m.id = p.modelId
        where b.id = %s
        """

        brand_id = (id,)
        logger.info('select_query {} with id {}', insert_query_to_select, brand_id)
        cur.execute(insert_query_to_select, brand_id)
        info = cur.fetchall()
        logger.debug('response from db = {}', info)
        return info

    except (Exception, psycopg2.Error) as error:
        if (connection):
            logger.error("Error {}", error)

    finally:
        if (connection):
            cur.close()
            connection.close()

@logger.catch()
def get_info_response(brand, model, year, price):
    model_list = []
    info = InfoForOneModel(brand=brand, model=model, year=year, price=price)
    model_list.append(info)
    return model_list

@logger.catch()
def get_brand_response(brand_info):
    brand_list = []
    for item in brand_info:
        brand = ResponseInfoForBrand(brand=item[0], model=item[1], year=item[2], price=item[3])
        brand_list.append(brand)
    return brand_list


class CarsInfo(cars_info_pb2_grpc.InfoServicer):
    @logger.catch()
    def GetInfoForModel(self, request, context):
        # ищем моель по id в базе
        car_info = select_data(request.modelId)
        logger.info('db response {}', car_info)

        if not car_info:
            logger.warning("Model with this modelId was not found")
            return ResponseForOneModel(info=[])
            # context.abort(grpc.StatusCode.NOT_FOUND, "Car not found")
        brand, model, year, price = car_info
        response = get_info_response(brand, model, year, price)
        return ResponseForOneModel(info=response)

    @logger.catch()
    def GetInfoForBrand(self, request, context):
        brand_info = select_brand(request.brandId)
        if not brand_info:
            logger.warning("Brand with this brandId was not found")
            return ResponseInfoForBrand([])

        response = get_brand_response(brand_info)

        for item in response:
            yield item

@logger.catch()
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cars_info_pb2_grpc.add_InfoServicer_to_server(
        CarsInfo(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
