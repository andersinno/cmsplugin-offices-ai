# -*- coding: utf-8 -*-
import pytest

from cmsplugin_offices_ai.models.personnel import Person
from tests.utils import create_personnel


@pytest.mark.django_db
def test_personnel_visibility():
    create_personnel(amount=10)
    for hidden_person in Person.objects.all()[:3]:
        hidden_person.show_in_list = False
        hidden_person.save()
    assert Person.objects.public().count() == 7
