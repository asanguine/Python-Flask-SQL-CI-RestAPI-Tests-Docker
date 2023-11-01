
import factory, random
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
from service.models.student import Student


class StudentFactory(factory.Factory):
    """ Creates fake Students """

    class Meta:
        model = Student

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    budget = factory.LazyAttribute(random.randrange(1000, 10000))

