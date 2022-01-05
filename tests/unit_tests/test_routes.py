from tests.conftest import client

import server
from server import create_app


def test_index_should_return_status_code_ok_and_normal_content(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
    assert b"Please enter your secretary email to continue:" in response.data
    assert b"Email:" in response.data


def test_index_should_return_normal_content(client):
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

    def test_showSummary_should_return_status_code_ok(self, client, mocker):
        # mocker.patch(server.loadClubs(), return_value=self.clubs)
        # mocker.patch(server.loadCompetitions(), return_value=self.competitions)
        # clubs = self.clubs
        response = client.get('/')
        assert response.status_code == 200
