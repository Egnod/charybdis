import pytest


@pytest.yield_fixture(scope="module")
def test_role(test_admin_client):
    role = test_admin_client.UserRole()
    role.slug = "test"

    role.save()

    yield role

    role.destroy()
