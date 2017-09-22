# -*- coding: utf-8 -*-
from cmsplugin_offices_ai.factories import OfficeFactory, DepartmentFactory, PersonFactory


def create_offices(amount):
    for _ in range(amount):
        OfficeFactory()


def create_departments(amount):
    for _ in range(amount):
        DepartmentFactory()


def create_personnel(amount):
    for _ in range(amount):
        PersonFactory()
