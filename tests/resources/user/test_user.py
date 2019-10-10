from ..util import check_read_only


def test_check_user(test_user):
    test_user = test_user.refresh()

    assert test_user.first_name == "123"
    assert test_user.last_name == "123"
    assert test_user.patronymic == "123"
    assert test_user.birthday == "2019-10-29"
    assert test_user.username == "test"
    assert test_user.domain_id and test_user.role_id
    assert test_user.uuid


def test_domain_read_only_check(test_user):
    fields = ["uuid"]

    check_read_only(fields, test_user)


def test_domain_deactivate(test_user):
    assert test_user.is_active

    test_user.deactivate()

    assert not test_user.refresh().is_active


def test_user_activate(test_user):
    assert not test_user.is_active

    test_user.activate()

    assert test_user.refresh().is_active


def test_user_update(test_user):
    test_user.first_name = "321"
    test_user.last_name = "321"
    test_user.patronymic = "321"
    test_user.birthday = "2019-10-25"
    test_user.username = "test1"

    test_user.save()


def test_user_after_update(test_user):
    test_user = test_user.refresh()

    assert test_user.first_name == "321"
    assert test_user.last_name == "321"
    assert test_user.patronymic == "321"
    assert test_user.birthday == "2019-10-25"
    assert test_user.username == "test1"
