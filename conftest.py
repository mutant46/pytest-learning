import pytest
from pytest_factoryboy import register
from app1.tests.factories import UserFactory, ProductFactory, CategoryFactory

''' Intro to Factories '''

@pytest.fixture
def user_1(db):
    ''' creating a user instance '''
    user = User.objects.create_user('test', 'test@test.com', 'test')
    return user


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = "test",
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory('test_user', 'test', )



@pytest.fixture
def create_superuser(db, new_user_factory):
    return new_user_factory('test_superuser', 'test', is_staff=True, is_superuser=True)



''' factoryboy conf '''

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def new_user(db, user_factory):
    user = user_factory(is_staff = True)
    return user

