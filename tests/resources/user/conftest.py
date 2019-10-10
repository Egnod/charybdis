import pytest


@pytest.yield_fixture(scope="module")
def test_role(test_admin_client):
    role = test_admin_client.UserRole()
    role.slug = "test"

    role.save()

    yield role

    role.destroy()


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
def test_user(test_admin_client, test_domain, test_role):
    user = test_admin_client.User()
    role = test_role
    domain = test_domain

    user.first_name = "123"
    user.last_name = "123"
    user.patronymic = "123"

    user.birthday = "2019-10-29"

    user.username = "test"

    user.domain_id = domain.id
    user.role_id = role.id

    user.save()
    user.change_password(new_password="123")

    yield user

    user.destroy()
