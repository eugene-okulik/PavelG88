class BaseClient:
    def __init__(self, base_url, session):
        self.base_url = base_url.rstrip('/')
        self.session = session
        self.response = None
        self.json = None

    def _save(self, response):
        self.response = response
        try:
            self.json = response.json()
        except ValueError:
            self.json = None

    def check_status(self, expected):
        assert self.response is not None
        assert self.response.status_code == expected, \
            f"Expected {expected}, got {self.response.status_code}"

    def check_fields(self, expected: dict):
        assert self.json is not None, "No JSON in response"

        for key, expected_value in expected.items():
            actual_value = self.json.get(key)
            assert actual_value == expected_value, \
                f"{key}: expected {expected_value}, got {actual_value}"
