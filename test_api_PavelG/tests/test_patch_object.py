import allure

from test_api_PavelG.endpoints.patch_object import PatchObject


@allure.epic("Object API")
@allure.feature("Обновление объекта")
@allure.story("Частичное обновление объекта (PATCH)")
def test_patch_object(new_obj):
    patcher = PatchObject()

    payload = {
        "name": "patched_name"
    }

    with allure.step("Отправляем PATCH запрос"):
        patcher.patch(new_obj, payload)

    patcher.check_status_200()

    with allure.step("Проверяем результат"):
        assert patcher.json["name"] == payload["name"]
