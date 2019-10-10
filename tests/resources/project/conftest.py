import pytest


@pytest.yield_fixture(scope="module")
def test_domain_project(test_admin_client):
    domain = test_admin_client.Domain()
    domain.slug = "test-project"
    domain.name = "Test Domain"
    domain.description = "Test" * 10
    domain.save()

    yield domain

    domain.destroy()


@pytest.yield_fixture(scope="module")
def test_domain(test_admin_client):
    domain = test_admin_client.Domain()
    domain.slug = "test"
    domain.name = "Test Domain"
    domain.description = "Test" * 10
    domain.save()

    yield domain

    domain.destroy()


@pytest.yield_fixture(scope="module")
def test_project(test_admin_client, test_domain):
    project = test_admin_client.Project()
    project.slug = "test"
    project.name = "Test"
    project.description = project.name * 10

    project.domain_id = test_domain.id

    project.save()

    yield project

    project.destroy()
