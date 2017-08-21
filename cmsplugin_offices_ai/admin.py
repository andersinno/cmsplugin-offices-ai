# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cmsplugin_offices_ai.models import Department, Office, Person
from cmsplugin_offices_ai.models.information_entries import ContactInformationEntry


class ContactInformationEntryInline(admin.TabularInline):
    model = ContactInformationEntry
    fieldsets = (
        ('', {
            'fields': ('value', 'entry_type'),
        }),
    )
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'order_no')
    search_fields = ('name', 'office')
    inlines = (ContactInformationEntryInline,)
    fieldsets = (
        ('', {
            'fields': (
                'name', 'description', 'office',
            )
        }),
        (_('Display options'), {
            'fields': (
                'order_no',
            )
        }),
    )


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'order_no')
    search_fields = ('name', 'city', 'country', 'order_no')
    inlines = (ContactInformationEntryInline,)
    fieldsets = (
        ('', {
            'fields': (
                'name', 'description',
            )
        }),
        (_('Address'), {
            'fields': (
                ('street_address', 'postal_code'), ('city', 'country'),
            ),
        }),
        (_('Display options'), {
            'fields': (
                'order_no',
            ),
        }),
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'show_in_list')
    search_fields = ('name', 'title')
    inlines = (ContactInformationEntryInline,)
    fieldsets = (
        ('', {
            'fields': (
                'name', 'title', 'image',
            )
        }),
        ('', {
            'fields': (
                'department', 'office_override',
            ),
            'classes': ('wide',),
        }),
        (_('Display options'), {
            'fields': (
                'show_in_list', 'order_no',
            )
        }),
    )
