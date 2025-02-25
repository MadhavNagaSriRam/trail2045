from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host="localhost:8000"
    wait_time = between(1, 1)

    @task
    def load_secure_page(self):
        # Payload data to be sent in the POST request
        payload = {
  "name": "madhav",
  "ph": 6300521118,
  "email": "mattaparthimadhav@gmail.com"
}

        # Simulate a POST request to the specified endpoint with payload data
        self.client.post("/locustt", json=payload) 