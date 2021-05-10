from server import CarsInfo
from cars_info_pb2 import RequestForOneModel
from loguru import logger
logger.add('debug_test.log', format="{time},{level},{message}", level='DEBUG')


def test_server():
    service = CarsInfo()
    request = RequestForOneModel(
        modelId=1,
    )
    response = service.GetInfoForModel(request, None)
    assert len(response.info) == 1
    assert  response.info[0].brand == "AUDI"

def test_server1():
    service = CarsInfo()
    request = RequestForOneModel(
        modelId=15,
    )
    response = service.GetInfoForModel(request, None)
    logger.debug(response)
    assert response is not None

    # assert  response.info[0].brand == "AUDI"