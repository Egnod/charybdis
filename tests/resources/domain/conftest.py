import pytest


@pytest.yield_fixture(scope="module")
def test_domain(test_admin_client):
    domain = test_admin_client.Domain()
    domain.slug = "test"
    domain.name = "Test Domain"
    domain.description = "Test" * 10
    domain.save()

    yield domain

    domain.destroy()
