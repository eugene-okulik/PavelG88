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

    def check_field(self, key, expected):
        assert self.json is not None, "No JSON in response"
        assert key in self.json, f"{key} not found in response JSON"
        assert self.json[key] == expected, \
            f"{key}: expected {expected}, got {self.json[key]}"
