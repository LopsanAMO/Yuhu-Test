import factory
from yuhutest.apps.tasks.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('sentence', nb_words=10)
    due_date = factory.Faker('date_time')
    user = factory.SubFactory('yuhutest.apps.users.tests.factories.UserFactory')