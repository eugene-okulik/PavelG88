import requests
import allure

from test_api_PavelG.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step("Обновить объект (PUT)")
    def put(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.put(
            f"{self.url}/{obj_id}",
            json=payload,
            headers=headers
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None

        return self.response
