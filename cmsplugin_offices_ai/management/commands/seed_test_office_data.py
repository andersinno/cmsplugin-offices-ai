# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from cmsplugin_offices_ai.factories import (
    DepartmentFactory, OfficeFactory, PersonFactory
)

class Command(BaseCommand):

    help = 'Creates fake test offices, departments and personnel.'

    def handle(self, *args, **options):
        for number in range(5):
            office = OfficeFactory()
            print('  %s. office: %s' % (number + 1, office.name))

        for number in range(20):
            department = DepartmentFactory()
            print('  %s.  department: %s' % (number + 1, department.name))

        for number in range(50):
            person = PersonFactory()
            print('  %s.  person: %s' % (number + 1, person.name))
