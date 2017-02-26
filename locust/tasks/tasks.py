from locust import HttpLocust, TaskSet, task
import json, requests

class Tasks(TaskSet):
    @task(1)
    def status(self):
        self.client.get("/")

class Warmer(HttpLocust):
    task_set = Tasks
    min_wait = 1000
    max_wait = 3000
