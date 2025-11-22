import allure


class Endpoint:
    base_url = "http://objapi.course.qa-practice.com"
    resource = "object"   # путь к ресурсу, меняется у наследников если надо

    response = None
    json = None
    headers = {"Content-type": "application/json"}

    @property
    def url(self):
        return f"{self.base_url}/{self.resource}"

    @allure.step("Проверка, что статус код = 200")
    def check_status_200(self):
        assert self.response.status_code == 200, \
            f"Expected 200, got {self.response.status_code}"
