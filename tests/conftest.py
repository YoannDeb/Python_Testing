import pytest
import server


@pytest.fixture
def client():
    """
    A pytest fixture to provide a test client for tests.
    :yield: client
    """
    with server.app.test_client() as client:
        yield client
