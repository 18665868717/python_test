from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)
    test_nub=1

    @task
    def my_task(self):
        self.client.get("/")
        print(self.test_nub)
        self.test_nub+=1