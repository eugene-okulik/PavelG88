import requests
import pytest

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
    response = requests.post(BASE_URL, json=body)
    obj_id = response.json()["id"]

    yield obj_id

    requests.delete(f"{BASE_URL}/{obj_id}")


@pytest.mark.critical
@pytest.mark.parametrize(
    "name,data",
    [
        ("object_1", {"info": "data1"}),
        ("object_2", {"info": "data2"}),
        ("object_3", {"info": "data3"}),
    ]
)
def test_create_object(name, data):
    body = {"name": name, "data": data}
    response = requests.post(BASE_URL, json=body)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["name"] == name
    assert resp_json["data"] == data


def test_put_object(new_obj):
    body = {"name": "updated_name", "data": {"info": "updated_data"}}
    response = requests.put(f"{BASE_URL}/{new_obj}", json=body)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["name"] == "updated_name"
    assert resp_json["data"]["info"] == "updated_data"


@pytest.mark.medium
def test_patch_object(new_obj):
    body = {"name": "patched_name"}
    response = requests.patch(f"{BASE_URL}/{new_obj}", json=body)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["name"] == "patched_name"


def test_delete_object(new_obj):
    response_delete = requests.delete(f"{BASE_URL}/{new_obj}")
    assert response_delete.status_code == 200

    response_get = requests.get(f"{BASE_URL}/{new_obj}")
    assert response_get.status_code == 404
