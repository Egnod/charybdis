from ..util import check_read_only


def test_project_check(test_project):
    test_project = test_project.refresh()

    assert test_project.id
    assert not test_project._uuid
    assert test_project.slug == "test"
    assert test_project.name == "Test"
    assert test_project.description == "Test" * 10
    assert test_project.domain_id
    assert test_project.is_active


def test_domain_read_only_check(test_project):
    fields = ["_uuid"]

    check_read_only(fields, test_project)


def test_project_update(test_project, test_domain_project):
    test_project.slug = "test1"
    test_project.name = "Test1"
    test_project.description = test_project.name * 10

    assert test_domain_project.id != test_project.domain_id

    test_project.domain_id = test_domain_project.id

    test_project.save()

    test_project = test_project.refresh()

    assert test_project.slug == "test1"
    assert test_project.name == "Test1"
    assert test_project.description == test_project.name * 10
    assert test_project.domain_id == test_domain_project.id


def test_project_uuid_cache(test_project):
    test_project.uuid()
    assert test_project.refresh()._uuid


def test_project_deactivate(test_project):
    assert test_project.is_active

    test_project.deactivate()

    test_project = test_project.refresh()

    assert not test_project.is_active


def test_project_activate(test_project):
    assert not test_project.is_active

    test_project.activate()

    test_project = test_project.refresh()

    assert test_project.is_active
