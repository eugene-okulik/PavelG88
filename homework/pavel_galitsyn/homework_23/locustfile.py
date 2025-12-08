from locust import HttpUser, task


class MemeUser(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            "/object",
            json={
                "name": "Locust object",
                "data": {
                    "color": "red",
                    "size": "big",
                },
            },
        )
        self.object_id = response.json()["id"]

    @task(3)
    def get_object_by_id(self):
        self.client.get(f"/object/{self.object_id}")

    @task(1)
    def get_all_objects(self):
        self.client.get("/object")
