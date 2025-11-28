import allure

@allure.epic("Object API")
@allure.feature("Удаление объекта")
def test_delete_object(deleter, getter, new_obj):

    with allure.step("Удаляем объект"):
        deleter.delete(new_obj)
        deleter.check_status(200)

    with allure.step("Проверяем что объект не найден"):
        getter.get(new_obj)
        getter.check_status(404)
