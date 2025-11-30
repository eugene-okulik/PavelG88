from .base import BaseClient


class GetObject(BaseClient):
    def get(self, obj_id):
        resp = self.session.get(f"{self.base_url}/{obj_id}")
        self._save(resp)
        return resp
