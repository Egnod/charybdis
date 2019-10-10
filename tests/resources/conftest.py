import pytest
from scylla import Client


@pytest.fixture(scope="session")
def test_admin_client():
    client = Client()

    return client


@pytest.fixture(scope="session")
def test_reader_user(test_admin_client):
    reader = test_admin_client.User()
    reader_role = test_admin_client.UserRole.instances(where={"slug": "reader"})[0]
    domain = test_admin_client.Domain.instances(where={"slug": "global"})[0]

    reader.first_name = "123"
    reader.last_name = "321"

    reader.birthday = "2019-10-29"

    reader.username = "reader"

    reader.domain_id = domain.id
    reader.role_id = reader_role.id

    reader.save()
    reader.change_password("123")

    return reader


@pytest.fixture(scope="session")
def test_reader_client(test_reader_user):
    client = Client(username=test_reader_user.username, password="123")

    return client
