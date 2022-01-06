from tests.conftest import client

import server
from server import create_app


def test_index_should_return_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_should_return_expected_content(client):
    response = client.get('/')
    data = response.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert "Please enter your secretary email to continue:" in data
    assert "Email:" in data


def test_index_should_return_status_code_405_on_post_request(client):
    response = client.post('/')
    assert response.status_code == 405


class TestShowSummary:

    clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }]

    competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]

    def test_showSummary_should_return_status_code_ok_with_secretary_email(self, client):
        # mocker.patch(server.loadClubs(), return_value=self.clubs)
        # mocker.patch(server.loadCompetitions(), return_value=self.competitions)
        # mocker.patch.object(server.create_app, 'clubs', self.clubs)
        clubs = self.clubs
        competitions = self.competitions
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_secretary_email(self, client):
        clubs = self.clubs
        competitions = self.competitions
        response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        data = response.data.decode()
        assert "Welcome, admin@irontemple.com" in data
        assert "Points available:" in data
        assert "Competitions:" in data
        assert "Spring Festival" in data
        assert "Date: 2020-03-27 10:00:00" in data
        assert "Number of Places:" in data

    def test_showSummary_should_return_status_code_ok_with_unknown_email(self, client):
        clubs = self.clubs
        competitions = self.competitions
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_unknown_email(self, client):
        clubs = self.clubs
        competitions = self.competitions
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        data = response.data.decode()
        assert "Welcome, test@test.com" in data
        assert "Points available:" in data
        assert "Competitions:" in data
        assert "Spring Festival" in data
        assert "Date: 2020-03-27 10:00:00" in data
        assert "Number of Places:" in data

    def test_showSummary_should_return_error_405_on_get_method(self, client):
        response = client.get('/showSummary')
        assert response.status_code == 405

