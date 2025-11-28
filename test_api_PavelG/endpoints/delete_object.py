import allure
from .base import BaseClient


class DeleteObject(BaseClient):

    @allure.step("Удалить объект (DELETE)")
    def delete(self, obj_id):
        resp = self.session.delete(f"{self.base_url}/{obj_id}")
        self._save(resp)
        return resp
