import requests
import pytest
import allure

BASE_URL = "http://objapi.course.qa-practice.com/object"


@pytest.fixture(scope="session", autouse=True)
def print_start_and_end():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def print_before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def new_obj():
    body = {"name": "test_name", "data": {"info": "test_data"}}
    with allure.step("Создание объекта в фикстуре"):
        response = requests.post(BASE_URL, json=body)
        allure.attach(str(response.json()), "Response", allure.attachment_type.JSON)

    obj_id = response.json()["id"]

    yield obj_id

    with allure.step("Удаление объекта после теста"):
        requests.delete(f"{BASE_URL}/{obj_id}")


@allure.epic("Object API")
@allure.feature("Создание объекта")
@allure.story("Создание объекта с разными payload")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "name,data",
    [
        ("object_1", {"info": "data1"}),
        ("object_2", {"info": "data2"}),
        ("object_3", {"info": "data3"}),
    ]
)
def test_create_object(name, data):
    with allure.step("Отправка POST-запроса на создание объекта"):
        body = {"name": name, "data": data}
        response = requests.post(BASE_URL, json=body)
        allure.attach(str(body), "Request body", allure.attachment_type.JSON)
        allure.attach(str(response.json()), "Response", allure.attachment_type.JSON)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json["name"] == name
        assert resp_json["data"] == data


@allure.epic("Object API")
@allure.feature("Обновление объекта")
@allure.story("PUT — Полное обновление объекта")
def test_put_object(new_obj):
    with allure.step("Отправка PUT-запроса"):
        body = {"name": "updated_name", "data": {"info": "updated_data"}}
        response = requests.put(f"{BASE_URL}/{new_obj}", json=body)
        allure.attach(str(body), "PUT Request body", allure.attachment_type.JSON)
        allure.attach(str(response.json()), "Response", allure.attachment_type.JSON)

    with allure.step("Проверка результата"):
        assert response.status_code == 200
        json = response.json()
        assert json["name"] == "updated_name"
        assert json["data"]["info"] == "updated_data"


@allure.epic("Object API")
@allure.feature("Обновление объекта")
@allure.story("PATCH — Частичное обновление объекта")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_object(new_obj):
    with allure.step("Отправка PATCH-запроса"):
        body = {"name": "patched_name"}
        response = requests.patch(f"{BASE_URL}/{new_obj}", json=body)
        allure.attach(str(body), "PATCH body", allure.attachment_type.JSON)
        allure.attach(str(response.json()), "Response", allure.attachment_type.JSON)

    with allure.step("Проверка результата"):
        assert response.status_code == 200
        assert response.json()["name"] == "patched_name"


@allure.epic("Object API")
@allure.feature("Удаление объекта")
@allure.story("Удаление и проверка что объект не существует")
def test_delete_object(new_obj):
    with allure.step("Удаление объекта"):
        response_delete = requests.delete(f"{BASE_URL}/{new_obj}")
        allure.attach(str(response_delete.status_code), "Delete status")
        assert response_delete.status_code == 200

    with allure.step("Проверка что объект удалён"):
        response_get = requests.get(f"{BASE_URL}/{new_obj}")
        allure.attach(str(response_get.status_code), "Get after delete status")
        assert response_get.status_code == 404
