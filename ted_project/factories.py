import factory
from django.contrib.auth.models import User
from ted.models import Face, Picture


class UserFactory(factory.django.DjangoModelFactory):
    """Defines a user for testing."""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class FaceFactory(factory.django.DjangoModelFactory):
    """Defines a recognized visitor instance for testing."""
    class Meta:
        model = Face

    name = 'test_name'


class PictureFactory(factory.django.DjangoModelFactory):
    """Defines an image url for testing."""
    class Meta:
        model = Picture

    face = factory.SubFactory(FaceFactory)
    url = 'test.url'
