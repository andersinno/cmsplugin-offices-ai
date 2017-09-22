# -*- coding: utf-8 -*-
import factory

from cmsplugin_offices_ai.models import Department, Office, Person
from cmsplugin_offices_ai.models.information_entries import ContactInformationEntry


class ContactInformationEntryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ContactInformationEntry


class DepartmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Department

    name = factory.Faker('word', locale='la')
    description = factory.Faker('catch_phrase', locale='en_GB')
    office = factory.Iterator(Office.objects.all())
    order_no = factory.Faker('random_int', min=0, max=1000)
    email = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'department',
        entry_type='email',
        value=factory.Faker('email', locale='en_GB')
    )
    phone = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'department',
        entry_type='phone',
        value=factory.Faker('phone_number', locale='en_GB')
    )
    fax = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'department',
        entry_type='fax',
        value=factory.Faker('phone_number', locale='en_GB')
    )


class OfficeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Office

    description = factory.Faker('catch_phrase', locale='en_GB')
    street_address = factory.Faker('street_address', locale='en_GB')
    postal_code = factory.Faker('postcode', locale='en_GB')
    city = factory.Faker('city', locale='en_GB')
    name = factory.LazyAttribute(lambda office: ('%s office' % office.city))
    order_no = factory.Faker('random_int', min=0, max=1000)
    email = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'office',
        entry_type='email',
        value=factory.Faker('email', locale='en_GB')
    )
    phone = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'office',
        entry_type='phone',
        value=factory.Faker('phone_number', locale='en_GB')
    )
    fax = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'office',
        entry_type='fax',
        value=factory.Faker('phone_number', locale='en_GB')
    )


class PersonFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Person

    name = factory.Faker('name', locale='en_GB')
    title = factory.Faker('word', locale='en_GB')
    description = factory.Faker('catch_phrase', locale='en_GB')
    department = factory.Iterator(Department.objects.all())
    order_no = factory.Faker('random_int', min=0, max=1000)
    email = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'person',
        entry_type='email',
        value=factory.Faker('email', locale='en_GB')
    )
    phone = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'person',
        entry_type='phone',
        value=factory.Faker('phone_number', locale='en_GB')
    )
    fax = factory.RelatedFactory(
        ContactInformationEntryFactory,
        'person',
        entry_type='fax',
        value=factory.Faker('phone_number', locale='en_GB')
    )
