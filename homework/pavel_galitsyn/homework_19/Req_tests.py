import requests

BASE_URL = "http://objapi.course.qa-practice.com/object"


def create_object():
    body = {
        "name": "new_name",
        "data": {"info": "new_data"}
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(BASE_URL, json=body, headers=headers)
    print("Status code:", response.status_code)
    print(response.json())

    obj_id = response.json()["id"]
    return obj_id


def put_object(obj_id):
    body = {
        "name": "updated_name",
        "data": {"info": "updated_data"}
    }
    response = requests.put(f"{BASE_URL}/{obj_id}", json=body)
    print("PUT:", response.status_code, response.json())


def patch_object(obj_id):
    body = {"name": "patched_name"}
    response = requests.patch(f"{BASE_URL}/{obj_id}", json=body)
    print("PATCH:", response.status_code, response.json())


def delete_object(obj_id):
    response = requests.delete(f"{BASE_URL}/{obj_id}")
    print("DELETE status:", response.status_code)
    print("Объект успешно удалён")


def run_all():
    obj_id = create_object()
    put_object(obj_id)
    patch_object(obj_id)
    delete_object(obj_id)


run_all()
