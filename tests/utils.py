import pytest
import server


def mock_load_Clubs_or_Competitions_empty():
    return {}


def mock_loadClubs_not_empty():
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
    return clubs


def mock_loadCompetitions_not_empty():
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
    return competitions


@pytest.fixture
def mock_normal_data_from_json(mocker):
    mocker.patch.object(server, 'clubs', mock_loadClubs_not_empty())
    mocker.patch.object(server, 'competitions', mock_loadCompetitions_not_empty())


@pytest.fixture
def mock_data_from_json_with_empty_clubs(mocker):
    mocker.patch.object(server, 'clubs', mock_load_Clubs_or_Competitions_empty())
    mocker.patch.object(server, 'competitions', mock_loadCompetitions_not_empty())


@pytest.fixture
def mock_data_from_json_with_empty_competitions(mocker):
    mocker.patch.object(server, 'clubs', mock_loadClubs_not_empty())
    mocker.patch.object(server, 'competitions', mock_load_Clubs_or_Competitions_empty())


@pytest.fixture
def mock_empty_data_from_json(mocker):
    mocker.patch.object(server, 'clubs', mock_load_Clubs_or_Competitions_empty())
    mocker.patch.object(server, 'competitions', mock_load_Clubs_or_Competitions_empty())
