from locust import HttpUser, task


class GUDLFT(HttpUser):
    @task
    def index(self):
        """
        Locust's task for index page.
        """
        self.client.get("/")

    @task
    def pointsDisplay(self):
        """
        Locust's task for pointsDisplay page.
        """
        self.client.get("/pointsDisplay")

    @task
    def showSummary(self):
        """
        Locust's task for showSummary page.
        """
        self.client.post("/showSummary", data={'email': 'john@simplylift.co'})

    @task
    def book(self):
        """
        Locust's task for book page.
        """
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchasePlaces(self):
        """
        Locust's task for purchasePlaces page.
        """
        self.client.post("/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '1'})
