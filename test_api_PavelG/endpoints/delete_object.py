import requests
import allure

from test_api_PavelG.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Удалить объект (DELETE)")
    def delete(self, obj_id, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.delete(
            f"{self.url}/{obj_id}",
            headers=headers
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None

        return self.response
