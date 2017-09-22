# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _


@python_2_unicode_compatible
class Office(models.Model):
    name = models.CharField(
        verbose_name=_('office name'),
        max_length=128,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=512,
        blank=True,
    )

    # Address
    street_address = models.CharField(
        verbose_name=_('street address'),
        max_length=128,
        blank=True,
    )
    postal_code = models.CharField(
        verbose_name=_('postal code'),
        max_length=16,
        blank=True,
    )
    city = models.CharField(
        verbose_name=_('city'),
        max_length=64,
        blank=True,
    )
    country = models.CharField(
        verbose_name=_('country'),
        max_length=128,
        blank=True,
    )

    # Display options
    order_no= models.PositiveSmallIntegerField(
        verbose_name=_('order no'),
        default=0,
        help_text=_('Determines the order in which offices are shown in. Smallest values first.')
    )

    class Meta:
        verbose_name = _('office')
        verbose_name_plural = _('offices')
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def address(self):
        return "{street_address}, {postal_code} {city}".format(
            street_address=self.street_address,
            postal_code=self.postal_code,
            city=self.city
        )

    @property
    def international_address(self):
        return "{address}, {country}".format(
            address=self.address,
            country=self.country
        )

    @property
    def google_maps_embed_q(self):
        """
        Returns the `q` GET parameter for Google Maps embed url.
        """
        return "{address}+{postal_code}+{city}+{country}".format(
            address=self.street_address,
            city=self.city,
            postal_code=self.postal_code,
            country=self.country,
        ).replace(" ", "")
