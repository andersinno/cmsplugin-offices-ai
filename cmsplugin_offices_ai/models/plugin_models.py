# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cmsplugin_offices_ai.models import Department, Office, Person


@python_2_unicode_compatible
class DepartmentListPlugin(CMSPlugin):
    """
    Plugin model for displaying selected departments.
    """
    departments = models.ManyToManyField(
        Department,
        verbose_name=_('department'),
        related_name='department_list_plugins',
    )
    show_personnel = models.BooleanField(
        verbose_name=_('show personnel'),
        default=False,
        help_text=_('Show personnel belonging to each department.')
    )

    def __str__(self):
        count = self.departments.all().count()
        if count == 1:
            return _('Department (%s)') % self.departments.first().name
        return _('Departments (amount: %s)') % count

    def copy_relations(self, old_instance):
        # This makes sure that the plugin's relations are copied during draft
        # publishing. Without this departments wouldn't be copied to the published
        # version of this object.
        # Docs: http://docs.django-cms.org/en/latest/how_to/custom_plugins.html#for-many-to-many-or-foreign-key-relations-to-other-objects  # NOQA
        self.departments = old_instance.departments.all()


@python_2_unicode_compatible
class OfficeListPlugin(CMSPlugin):
    """
    Plugin model for displaying selected offices.
    """
    offices = models.ManyToManyField(
        Office,
        verbose_name=_('office'),
        related_name='office_list_plugins',
    )
    show_map_embeds = models.BooleanField(
        verbose_name=_('show map embeds'),
        default=False,
    )

    def __str__(self):
        count = self.offices.all().count()
        if count == 1:
            return _('Office (%s)') % self.offices.first().name
        return _('Offices (amount: %s)') % count

    def copy_relations(self, old_instance):
        # This makes sure that the plugin's relations are copied during draft
        # publishing. Without this offices wouldn't be copied to the published
        # version of this object.
        # Docs: http://docs.django-cms.org/en/latest/how_to/custom_plugins.html#for-many-to-many-or-foreign-key-relations-to-other-objects  # NOQA
        self.offices = old_instance.offices.all()


@python_2_unicode_compatible
class PersonnelListPlugin(CMSPlugin):
    """
    Plugin model for displaying selected personnel.
    """
    personnel = models.ManyToManyField(
        Person,
        verbose_name=_('personnel'),
        related_name='personnel_list_plugins',
    )

    def __str__(self):
        count = self.personnel.all().count()
        if count == 1:
            return _('Person (%s)') % self.personnel.first().name
        return _('Personnel (amount: %s)') % count

    def copy_relations(self, old_instance):
        # This makes sure that the plugin's relations are copied during draft
        # publishing. Without this personnel wouldn't be copied to the published
        # version of this object.
        # Docs: http://docs.django-cms.org/en/latest/how_to/custom_plugins.html#for-many-to-many-or-foreign-key-relations-to-other-objects  # NOQA
        self.personnel = old_instance.personnel.all()
