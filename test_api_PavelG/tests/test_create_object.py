import allure
from test_api_PavelG.endpoints.create_object import CreateObject


@allure.epic("Object API")
@allure.feature("Создание объекта")
@allure.story("Успешное создание объекта")
def test_create_object():
    creator = CreateObject()

    payload = {
        "name": "object_name",
        "data": {"info": "some_info"}
    }

    with allure.step("Отправляем POST запрос"):
        creator.create(payload)

    creator.check_status_200()

    with allure.step("Проверяем поля в ответе"):
        assert creator.json["name"] == payload["name"]
        assert creator.json["data"] == payload["data"]
