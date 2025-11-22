import allure
import requests

from test_api_PavelG.endpoints.delete_object import DeleteObject


@allure.epic("Object API")
@allure.feature("Удаление объекта")
@allure.story("Успешное удаление объекта")
def test_delete_object(new_obj):
    deleter = DeleteObject()

    with allure.step("Отправляем DELETE запрос"):
        response = deleter.delete(new_obj)

    # Проверяем, что объект удалён
    assert response.status_code == 200

    with allure.step("Пробуем получить удалённый объект — должно быть 404"):
        url = f"{deleter.url}/{new_obj}"
        resp_get = requests.get(url)
        assert resp_get.status_code == 404
