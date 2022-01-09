import pytest
import server

from tests.utils import mock_loadClubs_not_empty, mock_loadCompetitions_not_empty


@pytest.fixture
def client():
    with server.app.test_client() as client:
        yield client
