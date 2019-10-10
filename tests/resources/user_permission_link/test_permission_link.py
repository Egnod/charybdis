def test_check_link(test_user_permission_link, test_project, test_permission, test_user):
    test_user_permission_link = test_user_permission_link.refresh()

    assert test_user_permission_link.permission_id == test_permission.id
    assert test_user_permission_link.user_id == test_user.id
    assert test_user_permission_link.project_id == test_project.id
