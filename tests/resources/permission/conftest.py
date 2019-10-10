import pytest


@pytest.yield_fixture(scope="module")
def test_permission(test_admin_client):
    permission = test_admin_client.Permission()
    permission.slug = "test"

    permission.save()

    yield permission

    permission.destroy()
