def test_permission_check(test_permission):
    test_permission = test_permission.refresh()

    assert test_permission.id
    assert test_permission.slug == "test"


def test_permission_update(test_permission):
    test_permission.slug = "test1"

    test_permission.save()


def test_check_permission_after_update(test_permission):
    test_permission = test_permission.refresh()

    assert test_permission.slug == "test1"
