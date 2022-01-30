import pytest
import server


def mock_load_Clubs_or_Competitions_empty():
    """
    Mock function to return empty dictionary instead of normal loadClubs or loadCompetitions returns.
    :return: An empty dictionary.
    """
    return {}


def mock_loadClubs_not_empty():
    """
    Mock function to return custom test dictionary instead of normal loadClubs return.
    :return: A custom dictionary.
    """
    clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "45"
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
    return clubs


def mock_loadCompetitions_not_empty():
    """
    Mock function to return custom test dictionary instead of normal loadCompetitions return.
    :return: A custom dictionary.
    """
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2029-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2029-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Past competition",
            "date": "2020-05-07 13:45:00",
            "numberOfPlaces": "42"
        },
    ]
    return competitions


@pytest.fixture
def mock_normal_data_from_json(mocker):
    """
    Pytest fixture to mock normal test data.
    :param mocker: Mocker fixture from pytest-mock plugin.
    """
    mocker.patch.object(server, 'clubs', mock_loadClubs_not_empty())
    mocker.patch.object(server, 'competitions', mock_loadCompetitions_not_empty())


@pytest.fixture
def mock_data_from_json_with_empty_clubs(mocker):
    """
    Pytest fixture to mock normal competitions' data and empty clubs.
    :param mocker: Mocker fixture from pytest-mock plugin.
    """
    mocker.patch.object(server, 'clubs', mock_load_Clubs_or_Competitions_empty())
    mocker.patch.object(server, 'competitions', mock_loadCompetitions_not_empty())


@pytest.fixture
def mock_data_from_json_with_empty_competitions(mocker):
    """
    Pytest fixture to mock normal clubs' data and empty competitions.
    :param mocker: Mocker fixture from pytest-mock plugin.
    """
    mocker.patch.object(server, 'clubs', mock_loadClubs_not_empty())
    mocker.patch.object(server, 'competitions', mock_load_Clubs_or_Competitions_empty())


@pytest.fixture
def mock_empty_data_from_json(mocker):
    """
    Pytest fixture to mock empty test data.
    :param mocker: Mocker fixture from pytest-mock plugin.
    """
    mocker.patch.object(server, 'clubs', mock_load_Clubs_or_Competitions_empty())
    mocker.patch.object(server, 'competitions', mock_load_Clubs_or_Competitions_empty())
