import pytest



''' Making a connection with database '''

@pytest.mark.django_db
def test_check_password(new_user):
    assert new_user.check_password('test') ==  True



