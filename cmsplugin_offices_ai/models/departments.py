# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cmsplugin_offices_ai.models.offices import Office


@python_2_unicode_compatible
class Department(models.Model):
    name = models.CharField(
        verbose_name=_('department name'),
        max_length=128,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=512,
        blank=True,
    )
    office = models.ForeignKey(
        Office,
        verbose_name=_('office'),
        related_name='departments',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # Display options
    order_no = models.PositiveSmallIntegerField(
        verbose_name=_('order no'),
        default=0,
        help_text=_('Determines the order in which departments are shown in. Smallest values first.')
    )

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        ordering = ['name']

    def __str__(self):
        return self.name
