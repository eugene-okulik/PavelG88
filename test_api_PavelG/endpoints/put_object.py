import allure
from .base import BaseClient


class PutObject(BaseClient):

    @allure.step("Обновить объект (PUT)")
    def put(self, obj_id, payload):
        resp = self.session.put(f"{self.base_url}/{obj_id}", json=payload)
        self._save(resp)
        return resp
