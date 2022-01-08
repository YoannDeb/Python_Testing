import pytest

from server import create_app
from tests.utils import mock_loadClubs_not_empty, mock_loadCompetitions_not_empty


@pytest.fixture
def client(mocker):
    app = create_app({"TESTING": True})
    # mocker.patch('server.loadClubs', return_value=mock_loadClubs_not_empty())
    # mocker.patch('server.loadCompetitions', return_value=mock_loadCompetitions_not_empty())
    # app.clubs = mock_loadClubs_not_empty()
    # app.competitions = mock_loadCompetitions_not_empty()
    with app.test_client() as client:
        yield client
