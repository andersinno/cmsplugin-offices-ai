# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugin_offices_ai.models import DepartmentListPlugin, OfficeListPlugin, PersonnelListPlugin


class DepartmentList(CMSPluginBase):
    model = DepartmentListPlugin
    module = _('Offices')
    name = _('Department list')
    render_template = 'cmsplugin_offices_ai/department_list.html'
    filter_horizontal = ('departments',)

    def render(self, context, instance, placeholder):
        departments = instance.departments.all().prefetch_related('department_contact_information').order_by('order_no')
        context.update({
            'instance': instance,
            'departments': departments,
            'placeholder': placeholder,
        })
        return context


class OfficeList(CMSPluginBase):
    model = OfficeListPlugin
    module = _('Offices')
    name = _('Office list')
    render_template = 'cmsplugin_offices_ai/office_list.html'
    fieldsets = (
        ('', {
            'fields': ('offices',)
        }),
        (_('Map settings'), {
            'fields': ('show_map_embeds',),
        }),
    )
    filter_horizontal = ('offices',)

    def render(self, context, instance, placeholder):
        offices = instance.offices.all().prefetch_related('office_contact_information').order_by('order_no')
        context.update({
            'instance': instance,
            'offices': offices,
            'placeholder': placeholder,
            'google_maps_api_key': getattr(settings, "GOOGLE_MAPS_API_KEY", None),
        })
        return context


class PersonnelList(CMSPluginBase):
    model = PersonnelListPlugin
    module = _('Offices')
    name = _('Personnel list')
    render_template = 'cmsplugin_offices_ai/personnel_list.html'
    filter_horizontal = ('personnel',)

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'personnel': instance.personnel.public().in_order(),
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(DepartmentList)
plugin_pool.register_plugin(OfficeList)
plugin_pool.register_plugin(PersonnelList)
