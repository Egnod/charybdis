def test_role_check(test_role):
    test_role = test_role.refresh()

    assert test_role.id
    assert test_role.slug == "test"


def test_role_update(test_role):
    assert test_role.slug == "test"

    test_role.slug = "test1"
    test_role.save()

    assert test_role.refresh().slug == "test1"
