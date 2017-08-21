# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from enumfields import Enum, EnumField

from cmsplugin_offices_ai.models.departments import Department
from cmsplugin_offices_ai.models.offices import Office
from cmsplugin_offices_ai.models.personnel import Person


class EntryType(Enum):
    EMAIL = 'email'
    PHONE = 'phone'
    FAX = 'fax'

    class Labels:
        EMAIL = _('email')
        PHONE = _('phone')
        FAX = _('fax')


@python_2_unicode_compatible
class ContactInformationEntry(models.Model):
    """
    Model class for different contact information entries
    person, department, or office might have.
    """
    entry_type = EnumField(EntryType, blank=False)
    value = models.CharField(
        verbose_name=_('value'),
        max_length=128,
        blank=False
    )

    person = models.ForeignKey(
        Person,
        verbose_name=_('person'),
        related_name='person_contact_information',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    office = models.ForeignKey(
        Office,
        verbose_name=_('office'),
        related_name='office_contact_information',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        Department,
        verbose_name=_('department'),
        related_name='department_contact_information',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Contact information entry')
        verbose_name_plural = _('Contact information entries')

    def __str__(self):
        return "Contact information entry"
