from tests.conftest import client
from urllib.parse import urlparse

import server
from server import create_app, loadCompetitions, loadClubs
from tests.utils import mock_loadClubs_not_empty


class TestIndex:

    def test_index_should_return_status_code_ok(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_index_should_return_expected_content(self, client):
        response = client.get('/')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
        assert "Email:" in data

    def test_index_should_return_status_code_405_on_post_request(self, client):
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

    def test_showSummary_should_return_status_code_ok_with_secretary_email(self, client, mocker):
        # mocker.patch(server.loadClubs, return_value=self.clubs)
        # mocker.patch(server.loadCompetitions(), return_value=self.competitions)
        # mocker.patch.object(server.create_app, 'clubs', self.clubs)
        # mocker.patch('loadClubs', return_value=self.clubs)
        # mocker.patch('server.loadClubs', return_value=self.clubs)
        print("clubs")
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_secretary_email(self, client):
        response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        data = response.data.decode()
        assert "Welcome, admin@irontemple.com" in data
        assert "Points available:" in data
        assert "Competitions:" in data
        assert "Spring Festival" in data
        assert "Date: 2020-03-27 10:00:00" in data
        assert "Number of Places:" in data

    def test_showSummary_should_return_status_code_ok_with_unknown_email(self, client):
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_unknown_email(self, client):
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

    # TODO: find how to mock loading of files and test with empty clubs list, empty competition list etc


class TestBook:

    def test_book_should_return_status_code_ok(self, client):
        response = client.get('/book/Spring Festival/Simply Lift')
        assert response.status_code == 200

    def test_book_should_return_expected_content(self, client):
        response = client.get('/book/Spring Festival/Simply Lift')
        data = response.data.decode()
        assert "Spring Festival" in data
        assert "Places available: 25" in data
        assert "How many places?" in data

    def test_book_should_return_status_code_405_on_post_method(self, client):
        response = client.post('/book/Spring Festival/Simply Lift')
        assert response.status_code == 405


class TestPurchasePlaces:

    def test_purchasePlaces_should_return_status_code_ok(self, client):
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        assert response.status_code == 200

    def test_purchasePlaces_should_return_correct_informations_after_booking_3_places(self, client):
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "Great-booking complete!" in data
        assert "Points available: 10" in data
        assert "Number of Places: 22" in data

    def test_purchasePlaces_should_return_correct_informations_after_booking_0_places(self, client):
        response = client.post('/purchasePlaces', data={'places': '0', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "Great-booking complete!" in data
        assert "Points available: 13" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_return_status_code_405_on_get_method(self, client):
        response = client.get('/purchasePlaces')
        assert response.status_code == 405

    def test_purchasePlaces_should_not_allow_negative_number_of_places(self, client):
        response = client.post('/purchasePlaces', data={'places': '-2', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "You can't book a negative number of places" in data
        assert "Great-booking complete!" not in data


class TestLogout:

    def test_logout_should_return_status_code_302_redirection(self, client):
        response = client.get('/logout')
        assert response.status_code == 302

    def test_logout_should_redirect_to_index(self, client):
        response = client.get('/logout')
        assert urlparse(response.location).path == '/'

    def test_logout_should_return_status_code_405_on_post_method(self, client):
        response = client.post('/logout')
        assert response.status_code == 405

