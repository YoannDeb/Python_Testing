from tests.conftest import client
from urllib.parse import urlparse

from tests.utils import mock_normal_data_from_json, mock_empty_data_from_json, mock_data_from_json_with_empty_clubs, mock_data_from_json_with_empty_competitions


class TestIndex:

    def test_index_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        response = client.get('/')
        assert response.status_code == 200

    def test_index_should_return_expected_content(self, client, mock_normal_data_from_json):
        response = client.get('/')
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data

    def test_index_should_return_status_code_405_on_post_request(self, client, mock_normal_data_from_json):
        response = client.post('/')
        assert response.status_code == 405


class TestShowSummary:

    def test_showSummary_should_return_status_code_ok_with_secretary_email(self, client, mock_normal_data_from_json):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_showSummary_should_return_expected_content_with_secretary_email(self, client, mock_normal_data_from_json):
        response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        data = response.data.decode()
        assert "Welcome, admin@irontemple.com" in data
        assert "Points available:" in data
        assert "Competitions:" in data
        assert "Spring Festival" in data
        assert "Date: 2029-03-27 10:00:00" in data
        assert "Number of Places:" in data

    def test_showSummary_should_return_status_code_ok_with_unknown_email(self, client, mock_normal_data_from_json):
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        assert response.status_code == 200

    # def test_showSummary_should_return_status_code_302_with_empty_email(self, client, mock_normal_data_from_json):
    #     response = client.post('/showSummary', data={'email': ''})
    #     assert response.status_code == 302

    def test_showSummary_should_return_expected_content_with_unknown_email(self, client, mock_normal_data_from_json):
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data
        assert "You are not secretary of a club. Please input a secretary email." in data

    # def test_showSummary_should_return_expected_content_with_empty_email(self, client, mock_normal_data_from_json):
    #     response = client.post('/showSummary', data={'email': ''})
    #     data = response.data.decode()
    #     assert "Welcome to the GUDLFT Registration Portal!" in data
    #     assert "Please enter your secretary email to continue:" in data

    def test_showSummary_should_return_302_on_get_method(self, client, mock_normal_data_from_json):
        response = client.post('/showSummary')
        assert response.status_code == 302

    def test_show_summary_should_return_status_code_ok_with_empty_data(self, client, mock_empty_data_from_json):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_show_summary_should_return_status_code_ok_with_empty_clubs(self, client, mock_data_from_json_with_empty_clubs):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200

    def test_show_summary_should_return_status_code_ok_with_empty_competitions(self, client, mock_data_from_json_with_empty_competitions):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200


class TestBook:

    def test_book_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        response = client.get('/book/Spring Festival/Simply Lift')
        assert response.status_code == 200

    def test_book_should_return_expected_content(self, client, mock_normal_data_from_json):
        response = client.get('/book/Spring Festival/Simply Lift')
        data = response.data.decode()
        assert "Spring Festival" in data
        assert "Places available: 25" in data
        assert "How many places?" in data

    def test_book_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
        response = client.post('/book/Spring Festival/Simply Lift')
        assert response.status_code == 405

    def test_book_should_not_allow_booking_for_past_competitions(self, client, mock_normal_data_from_json):
        response = client.post('/book/Past competition/Simply Lift')
        data = response.data.decode()
        assert "You can't book a place for past competitions."
        assert "Great-booking complete!" not in data


class TestPurchasePlaces:

    def test_purchasePlaces_should_return_status_code_ok(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert response.status_code == 200

    def test_purchasePlaces_should_return_correct_informations_after_booking_3_places(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '3', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "Great-booking complete!" in data
        assert "Points available: 10" in data
        assert "Number of Places: 22" in data

    def test_purchasePlaces_should_return_correct_informations_after_booking_0_places(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '0', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "The number of places must be greater than 0 to be valid." in data
        assert "Points available: 13" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_return_status_code_405_on_get_method(self, client, mock_normal_data_from_json):
        response = client.get('/purchasePlaces')
        assert response.status_code == 405

    def test_purchasePlaces_should_not_allow_negative_number_of_places(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '0', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Welcome, john@simplylift.co" in data
        assert "The number of places must be greater than 0 to be valid." in data
        assert "Points available: 13" in data
        assert "Number of Places: 25" in data

    def test_purchasePlaces_should_not_allow_booking_more_than_12_places_in_one_purchase(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '13', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "You can't book more than 12 places in a single competition."
        assert "Great-booking complete!" not in data

    def test_purchasePlaces_should_not_allow_booking_more_than_12_places_in_two_purchase(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '7', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        response = client.post('/purchasePlaces', data={'places': '6', 'club': 'Simply Lift', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "You can't book more than 12 places in a single competition."
        assert "Great-booking complete!" not in data


    def test_purchasePlaces_should_not_allow_booking_more_places_than_the_amount_of_points_the_club_has(self, client, mock_normal_data_from_json):
        response = client.post('/purchasePlaces', data={'places': '5', 'club': 'Iron Temple', 'competition': 'Spring Festival'})
        data = response.data.decode()
        assert "Club doesn't have enough points to book this amount of places."
        assert "Great-booking complete!" not in data


# class TestPointsDisplay:
#
#     def test_pointsDisplay_should_return_status_code_ok(self, client, mock_normal_data_from_json):
#         response = client.get('/pointsDisplay')
#         assert response.status_code == 200
#
#     def test_pointsDisplay_should_return_expected_content(self, client, mock_normal_data_from_json):
#         response = client.get('/pointsDisplay')
#         data = response.data.decode()
#         assert "Points Chart" in data
#         assert "Simply Lift" in data
#         # todo complete with more content when decided
#
#     def test_pointsDisplay_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
#         response = client.post('/pointsDisplay')
#         assert response.status_code == 405


class TestLogout:

    def test_logout_should_return_status_code_302_redirection(self, client, mock_normal_data_from_json):
        response = client.get('/logout')
        assert response.status_code == 302

    def test_logout_should_redirect_to_index(self, client, mock_normal_data_from_json):
        response = client.get('/logout')
        assert urlparse(response.location).path == '/'

    def test_logout_should_return_status_code_405_on_post_method(self, client, mock_normal_data_from_json):
        response = client.post('/logout')
        assert response.status_code == 405

