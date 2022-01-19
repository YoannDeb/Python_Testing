from locust import HttpUser, task


class GUDLFT(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def pointsDisplay(self):
        self.client.get("/pointsDisplay")

    @task
    def showSummary(self):
        self.client.post("/showSummary", data={'email': 'john@simplylift.co'})

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchasePlaces(self):
        self.client.post("/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '5'})

