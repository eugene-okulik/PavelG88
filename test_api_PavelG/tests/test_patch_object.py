import allure

@allure.epic("Object API")
@allure.feature("PATCH частичное обновление")
def test_patch_object(patcher, new_obj):
    payload = {"name": "patched_name"}

    with allure.step("Отправляем PATCH"):
        patcher.patch(new_obj, payload)
        patcher.check_status(200)

    with allure.step("Проверяем поля"):
        patcher.check_field("name", "patched_name")
