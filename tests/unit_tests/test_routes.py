from tests.conftest import client
from urllib.parse import urlparse

from tests.utils import mock_normal_data_from_json, mock_empty_data_from_json, mock_data_from_json_with_empty_clubs, mock_data_from_json_with_empty_competitions


class TestIndex:

    def test_index_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user goes to the index page
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/')
        assert response.status_code == 200

    def test_index_should_return_expected_content(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user goes to the index page
        THEN the app returns expected content.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data

    def test_index_should_return_status_code_405_on_post_request(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the index page
        THEN status code of the response is 405 (which means the action is not allowed).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/')
        assert response.status_code == 405


class TestShowSummary:

    def test_showSummary_should_return_status_code_ok_with_secretary_email(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the showSummary page with a secretary email inside it
        THEN status code of the response is 200.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_secretary_email(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the showSummary page with a secretary email inside it
        THEN the app returns expected content.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        data = response.data.decode()
        assert "Welcome, admin@irontemple.com" in data
        assert "Points available:" in data
        assert "Competitions:" in data
        assert "Spring Festival" in data
        assert "Date: 2029-03-27 10:00:00" in data
        assert "Number of Places:" in data

    def test_showSummary_should_return_status_code_ok_with_unknown_email(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the showSummary page with an unknown email inside it
        THEN status code of the response is 200.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_unknown_email(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the showSummary page with an unknown email inside it
        THEN the app returns expected content from index page with an error message.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
        assert "You are not secretary of a club. Please input a secretary email." in data

    def test_showSummary_should_return_302_on_get_method(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a GET request to the showSummary page
        THEN status code of the response is 302 (which means he is redirected).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/showSummary')
        assert response.status_code == 302

    def test_show_summary_should_return_status_code_ok_with_empty_data(self, client, mock_empty_data_from_json):
        """
        GIVEN a user is not logged on the app and the test data is empty
        WHEN the user sends a POST request to the showSummary page with a secretary email inside it
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_empty_data_from_json: Pytest fixture mocking db loading with empty test data.
        """
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_show_summary_should_return_status_code_ok_with_empty_clubs(self, client, mock_data_from_json_with_empty_clubs):
        """
        GIVEN a user is not logged on the app and the test data about clubs is empty
        WHEN the user sends a POST request to the showSummary page with a secretary email inside it
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_data_from_json_with_empty_clubs: Pytest fixture mocking db loading with test data for competitions
        but clubs data is empty.
        """
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_show_summary_should_return_status_code_ok_with_empty_competitions(self, client, mock_data_from_json_with_empty_competitions):
        """
        GIVEN a user is not logged on the app and the test data about competitions is empty
        WHEN the user sends a POST request to the showSummary page with a secretary email inside it
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_data_from_json_with_empty_clubs: Pytest fixture mocking db loading with test data for clubs
        but competitions data is empty.
        """
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200


class TestBook:

    def test_book_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the user chooses a competitions of which he wants to book places
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/Spring Festival/Simply Lift')
        assert response.status_code == 200

    def test_book_should_return_expected_content(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the user chooses a competitions of which he wants to book places
        THEN the app returns expected content.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/Spring Festival/Simply Lift')
        data = response.data.decode()
        assert "Spring Festival" in data
        assert "Places available: 25" in data
        assert "How many places?" in data

    def test_book_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the user sends a POST request to the book page
        THEN status code of the response is 405 (which means the action is not allowed).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/book/Spring Festival/Simply Lift')
        assert response.status_code == 405

    def test_book_should_not_allow_booking_for_past_competitions(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the user chooses a past competitions of which he wants to book places
        THEN the app returns expected content, the user can't access the book page and
        goes to the welcome page (showSummary route) with error message.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/Past competition/Simply Lift')
        data = response.data.decode()
        assert "You can&#39;t book a place for past competitions." in data
        assert "Great-booking complete!" not in data
        assert "Points available: 45" in data
        assert "Number of Places: 25" in data

    def test_book_should_return_error_message_when_competition_does_not_exist(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the club in the address does not exist
        THEN the app returns expected content, the user can't access the book page and
        goes to the welcome page (showSummary route) with error message.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/UnknownCompetition/Simply Lift')
        data = response.data.decode()
        assert "Something went wrong-please try again" in data
        assert "Great-booking complete!" not in data
        assert "Points available: 45" in data
        assert "Number of Places: 25" in data

    def test_book_should_return_error_message_when_club_does_not_exist(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the competition in the address does not exist
        THEN the app returns expected content, the user can't access the book page and
        goes to the index page with error message.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/Spring Festival/UnknownClub')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
        assert "Something went wrong, please enter your mail again." in data

    def test_book_should_return_error_message_when_competition_and_club_does_not_exist(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app and we know which club he is secretary of
        WHEN the club and competition in the address does not exist
        THEN the app returns expected content, the user can't access the book page and
        goes to the welcome page (showSummary route) with error message.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/book/UnknownCompetition/UnknownClub')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
        assert "Something went wrong, please enter your mail again." in data


class TestPurchasePlaces:

    def test_purchasePlaces_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user wants to order 3 places
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        assert response.status_code == 200

    def test_purchasePlaces_should_return_correct_informations_after_booking_3_places(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user wants to order 3 places
        THEN the points available for the club and the number of places of the competition are updated.
        A confirmation message is also shown.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "Great-booking complete!" in data
        assert "Points available: 36" in data
        assert "Number of Places: 22" in data

    def test_purchasePlaces_should_return_correct_informations_after_booking_0_places(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user wants to order 0 places
        THEN the points available for the club and the number of places of the competition stays the same.
        An information message is also shown.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '0', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "The number of places must be greater than 0 to be valid." in data
        assert "Points available: 45" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_return_status_code_405_on_get_method(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user sends a GET request to the purchasePlaces page
        THEN status code of the response is 405 (which means the action is not allowed).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/purchasePlaces')
        assert response.status_code == 405

    def test_purchasePlaces_should_not_allow_negative_number_of_places(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user wants to order -3 places
        THEN the points available for the club and the number of places of the competition stays the same.
        An information message is also shown.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '-3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "The number of places must be greater than 0 to be valid." in data
        assert "Points available: 45" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_not_allow_booking_more_than_12_places_in_one_purchase(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user wants to order 13 places
        THEN the points available for the club and the number of places of the competition stays the same.
        An information message is also shown.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '13', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "You can&#39;t book more than 12 places in a single competition." in data
        assert "Great-booking complete!" not in data
        assert "Points available: 45" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_not_allow_booking_more_than_12_places_in_two_purchase(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user orders 7 places then 6 places
        THEN the points available for the club and the number of places of the competition are updated for the
        first order, but the second order is not filled. An information message is also shown for the two orders.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '7', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Great-booking complete!" in data
        assert "Points available: 24" in data
        assert "Number of Places: 18" in data
        response = client.post('/purchasePlaces', data={'places': '6', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "You can&#39;t book more than 12 places in a single competition." in data
        assert "Great-booking complete!" not in data
        assert "Points available: 24" in data
        assert "Number of Places: 18" in data

    def test_purchasePlaces_should_not_allow_booking_more_places_than_the_amount_of_points_the_club_has(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged and as chosen a competition
        WHEN the user orders 5 places for a competition that only have 5 places avilable
        THEN the points available for the club and the number of places of the competition stays the same.
        An information message is also shown.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/purchasePlaces', data={'places': '5', 'club': 'Iron Temple', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Club doesn&#39;t have enough points to book this amount of places." in data
        assert "Great-booking complete!" not in data
        assert "Points available: 4" in data
        assert "Number of Places: 25" in data


class TestPointsDisplay:

    def test_pointsDisplay_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user wants to see the chart of points
        THEN status code of the response is 200 (which means ok).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/pointsDisplay')
        assert response.status_code == 200

    def test_pointsDisplay_should_return_expected_content(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user wants to see the chart of points
        THEN the app shows the score chart.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/pointsDisplay')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Score Chart!" in data
        assert "Simply Lift" in data
        assert "Available booking points" in data
        assert "45" in data

    def test_pointsDisplay_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the pointsDisplay page
        THEN status code of the response is 405 (which means the action is not allowed).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/pointsDisplay')
        assert response.status_code == 405


class TestLogout:

    def test_logout_should_return_status_code_302_redirection(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app
        WHEN the user goes to the logout page
        THEN status code of the response is 302 (which means redirection).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/logout')
        assert response.status_code == 302

    def test_logout_should_redirect_to_index(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is logged on the app
        WHEN the user goes to the logout page
        THEN the user is redirected to the index page.
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.get('/logout')
        assert urlparse(response.location).path == '/'

    def test_logout_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
        """
        GIVEN a user is not logged on the app
        WHEN the user sends a POST request to the logout page
        THEN status code of the response is 405 (which means the action is not allowed).
        :param client: Pytest fixture for test client in conftest.py.
        :param mock_normal_data_from_json: Pytest fixture mocking db loading with test data.
        """
        response = client.post('/logout')
        assert response.status_code == 405
