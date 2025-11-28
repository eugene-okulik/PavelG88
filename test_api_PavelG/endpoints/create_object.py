import allure
from .base import BaseClient


class CreateObject(BaseClient):

    @allure.step("Создать объект (POST)")
    def create(self, payload):
        resp = self.session.post(self.base_url, json=payload)
        self._save(resp)
        return resp
