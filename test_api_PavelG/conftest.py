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


@pytest.fixture
def creator(session):
    return CreateObject(BASE_URL, session)


@pytest.fixture
def getter(session):
    return GetObject(BASE_URL, session)


@pytest.fixture
def updater(session):
    return PutObject(BASE_URL, session)


@pytest.fixture
def patcher(session):
    return PatchObject(BASE_URL, session)


@pytest.fixture
def deleter(session):
    return DeleteObject(BASE_URL, session)


@pytest.fixture
def new_obj(creator, deleter):
    payload = {"name": "test_name", "data": {"info": "test_data"}}
    creator.create(payload)
    creator.check_status(200)

    obj_id = creator.json["id"]
    yield obj_id

    deleter.delete(obj_id)
