import pytest
import allure

from test_api_PavelG.endpoints.create_object import CreateObject
from test_api_PavelG.endpoints.delete_object import DeleteObject


@pytest.fixture()
def new_obj():
    """
    Создаёт объект перед тестом и удаляет его после теста.
    """
    creator = CreateObject()

    payload = {
        "name": "test_name",
        "data": {"info": "test_data"}
    }

    # Создание объекта
    with allure.step("Создание объекта (POST) через endpoint-класс"):
        creator.create(payload)
        creator.check_status_200()
        obj_id = creator.json["id"]

    yield obj_id

    # Удаление объекта
    deleter = DeleteObject()
    with allure.step("Удаление объекта (DELETE) через endpoint-класс"):
        deleter.delete(obj_id)
