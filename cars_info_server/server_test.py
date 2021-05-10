from server import CarsInfo
from cars_info_pb2 import RequestForOneModel, RequestForBrand
from loguru import logger
# from cars_info_server.server import CarsInfo
from unittest import TestCase
from unittest.mock import patch, Mock
from db_init import connect_to_db

logger.add('debug_test.log', format="{time},{level},{message}", level='DEBUG')


def test_db_connection():
    response = connect_to_db()
    assert response == "OK"


def test_get_info_for_model():
    service = CarsInfo()
    request = RequestForOneModel(
        modelId=3,
    )
    response = service.GetInfoForModel(request, None)

    assert response is not None
    assert len(response.info) == 1
    assert  response.info[0].brand == "AUDI"


def test_get_info_for_brand():
    service = CarsInfo()
    request = RequestForBrand(
        brandId=3,
    )
    response = service.GetInfoForBrand(request, None)
    assert response is not None
    assert len(list(response)) == 3
    # assert  response.info[0].brand == "AUDI"
# class TestBlog(TestCase):
#     @patch('CarsInfo')
#     def test_cars_info_get_for_one_model:
#         cars_info = MockCarsInfo()
#
#



