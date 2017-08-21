# -*- coding: utf-8 -*-
import pytest

from tests.utils import create_offices, create_departments, create_personnel


@pytest.mark.django_db
def test_factories():
    """
    Simple test that runs all factories. These should prevent anyone introducing
    breaking changes without a notice from Travis.
    """
    create_offices(amount=3)
    create_departments(amount=3)
    create_personnel(amount=10)
