import pytest
import allure

@allure.epic("Object API")
@allure.feature("Создание объекта")
@pytest.mark.parametrize(
    "name,data",
    [
        ("object_1", {"info": "data1"}),
        ("object_2", {"info": "data2"}),
        ("object_3", {"info": "data3"}),
    ]
)
def test_create_object(creator, name, data):
    payload = {"name": name, "data": data}

    with allure.step("Создаём объект"):
        creator.create(payload)
        creator.check_status(200)

    with allure.step("Проверяем поля"):
        creator.check_field("name", name)
        creator.check_field("data", data)
