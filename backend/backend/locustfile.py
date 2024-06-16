from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def login(self):
        response = self.client.post("http://127.0.0.1:8000/login/", json={
            "username": "test_user",
            "password": "test_password"
        })
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

        if response.status_code != 200:
            print("Login failed with status code:", response.status_code)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")
