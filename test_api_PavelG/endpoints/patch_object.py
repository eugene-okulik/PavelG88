from .base import BaseClient
import allure


class PatchObject(BaseClient):

    @allure.step("Частично обновить объект (PATCH)")
    def patch(self, obj_id, payload):
        resp = self.session.patch(f"{self.base_url}/{obj_id}", json=payload)
        self._save(resp)
        return resp
