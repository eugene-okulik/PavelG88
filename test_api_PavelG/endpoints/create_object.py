import requests
import allure

from test_api_PavelG.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step("Создать объект (POST)")
    def create(self, payload, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.post(
            self.url,          # ← формируется автоматически: base_url + resource
            json=payload,
            headers=headers
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None

        return self.response
