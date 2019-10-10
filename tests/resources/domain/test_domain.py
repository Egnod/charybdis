from ..util import check_read_only


def test_domain_check(test_domain):
    test_domain = test_domain.refresh()

    assert test_domain.id
    assert test_domain.uuid
    assert test_domain.slug == "test"
    assert test_domain.name == "Test Domain"
    assert test_domain.description == "Test" * 10


def test_domain_read_only_check(test_domain):
    fields = ["uuid"]

    check_read_only(fields, test_domain)


def test_domain_deactivate(test_domain):
    assert test_domain.is_active

    test_domain.deactivate()

    assert not test_domain.fetch(test_domain.id).is_active


def test_domain_activate(test_domain):
    assert not test_domain.is_active

    test_domain.activate()

    assert test_domain.fetch(test_domain.id).is_active


def test_domain_update(test_domain):
    assert test_domain.slug == "test"

    test_domain.slug = "test1"
    test_domain.save()

    assert test_domain.refresh().slug == "test1"
