import pytest
import requests

from test_api_PavelG.endpoints.create_object import CreateObject
from test_api_PavelG.endpoints.get_object import GetObject
from test_api_PavelG.endpoints.put_object import PutObject
from test_api_PavelG.endpoints.patch_object import PatchObject
from test_api_PavelG.endpoints.delete_object import DeleteObject

BASE_URL = "http://objapi.course.qa-practice.com/object"


@pytest.fixture(scope="session")
def session():
    return requests.Session()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def creator(base_url, session):
    return CreateObject(base_url, session)


@pytest.fixture
def getter(base_url, session):
    return GetObject(base_url, session)


@pytest.fixture
def updater(base_url, session):
    return PutObject(base_url, session)


@pytest.fixture
def patcher(base_url, session):
    return PatchObject(base_url, session)


@pytest.fixture
def deleter(base_url, session):
    return DeleteObject(base_url, session)


@pytest.fixture
def new_obj(creator, deleter):
    payload = {"name": "test_name", "data": {"info": "test_data"}}
    creator.create(payload)
    creator.check_status(200)

    obj_id = creator.json["id"]
    yield obj_id

    deleter.delete(obj_id)
