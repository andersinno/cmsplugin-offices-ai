# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from cmsplugin_offices_ai.models import Department, Office


class PersonQuerySet(models.QuerySet):

    def in_order(self):
        """
        Orders queryset by `order_no` field value
        """
        return self.order_by('order_no')

    def public(self):
        """
        Exclude personnel that are not supposed to be shown in lists from queryset.
        """
        return self.filter(show_in_list=True).prefetch_related('person_contact_information')


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=128,
        blank=False,
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=128,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=512,
        blank=True,
    )
    image = FilerImageField(
        verbose_name=_('image'),
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    office_override = models.ForeignKey(
        Office,
        verbose_name=_('office'),
        related_name='personnel_in_office',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Overrides the office the person is assumed to belong to via selected department.')
    )
    department = models.ForeignKey(
        Department,
        verbose_name=_('department'),
        related_name='personnel_in_department',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # Display options
    show_in_list = models.BooleanField(
        verbose_name=_('show in list'),
        default=True,
        help_text=_('Show this person in personnel list plugins.')
    )
    order_no = models.PositiveSmallIntegerField(
        verbose_name=_('order number'),
        default=0,
        help_text=_('Determines the order in which personnel are shown in. Smallest values first.')
    )

    objects = PersonQuerySet.as_manager()

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('personnel')
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def office(self):
        if self.office_override:
            return self.office_override
        return self.department.office
