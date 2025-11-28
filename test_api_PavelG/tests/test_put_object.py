import allure

@allure.epic("Object API")
@allure.feature("Обновление объекта")
def test_put_object(updater, getter, new_obj):
    payload = {"name": "updated_name", "data": {"info": "updated_data"}}

    with allure.step("Отправляем PUT"):
        updater.put(new_obj, payload)
        updater.check_status(200)

    with allure.step("Сверяем поля"):
        updater.check_field("name", "updated_name")
        updater.check_field("data", {"info": "updated_data"})
