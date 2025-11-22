import requests
import allure

from test_api_PavelG.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step("Частично обновить объект (PATCH)")
    def patch(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.patch(
            f"{self.url}/{obj_id}",
            json=payload,
            headers=headers
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None

        return self.response
