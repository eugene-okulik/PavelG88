import allure

from test_api_PavelG.endpoints.update_object import UpdateObject


@allure.epic("Object API")
@allure.feature("Обновление объекта")
@allure.story("Успешное полное обновление объекта (PUT)")
def test_put_object(new_obj):
    updater = UpdateObject()

    payload = {
        "name": "updated_name",
        "data": {"info": "updated_info"}
    }

    with allure.step("Отправляем PUT запрос"):
        updater.put(new_obj, payload)

    updater.check_status_200()

    with allure.step("Проверяем результат"):
        assert updater.json["name"] == payload["name"]
        assert updater.json["data"]["info"] == payload["data"]["info"]
