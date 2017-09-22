# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_offices_ai.models.information_entries
import filer.fields.image
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformationEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('entry_type', enumfields.fields.EnumField(enum=cmsplugin_offices_ai.models.information_entries.EntryType, max_length=10)),
                ('value', models.CharField(verbose_name='value', max_length=128)),
            ],
            options={
                'verbose_name': 'Contact information entry',
                'verbose_name_plural': 'Contact information entries',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='department name', max_length=128)),
                ('description', models.TextField(verbose_name='description', max_length=512, blank=True)),
                ('order_no', models.PositiveSmallIntegerField(verbose_name='order no', default=0, help_text='Determines the order in which departments are shown in. Smallest values first.')),
            ],
            options={
                'verbose_name': 'department',
                'ordering': ['name'],
                'verbose_name_plural': 'departments',
            },
        ),
        migrations.CreateModel(
            name='DepartmentListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_offices_ai_departmentlistplugin', auto_created=True, to='cms.CMSPlugin', parent_link=True, primary_key=True, serialize=False)),
                ('show_personnel', models.BooleanField(verbose_name='show personnel', default=False, help_text='Show personnel belonging to each department.')),
                ('departments', models.ManyToManyField(verbose_name='department', related_name='department_list_plugins', to='cmsplugin_offices_ai.Department')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='office name', max_length=128)),
                ('description', models.TextField(verbose_name='description', max_length=512, blank=True)),
                ('street_address', models.CharField(verbose_name='street address', max_length=128, blank=True)),
                ('postal_code', models.CharField(verbose_name='postal code', max_length=16, blank=True)),
                ('city', models.CharField(verbose_name='city', max_length=64, blank=True)),
                ('country', models.CharField(verbose_name='country', max_length=128, blank=True)),
                ('order_no', models.PositiveSmallIntegerField(verbose_name='order no', default=0, help_text='Determines the order in which offices are shown in. Smallest values first.')),
            ],
            options={
                'verbose_name': 'office',
                'ordering': ['name'],
                'verbose_name_plural': 'offices',
            },
        ),
        migrations.CreateModel(
            name='OfficeListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_offices_ai_officelistplugin', auto_created=True, to='cms.CMSPlugin', parent_link=True, primary_key=True, serialize=False)),
                ('show_map_embeds', models.BooleanField(verbose_name='show map embeds', default=False)),
                ('offices', models.ManyToManyField(verbose_name='office', related_name='office_list_plugins', to='cmsplugin_offices_ai.Office')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=128)),
                ('title', models.CharField(verbose_name='title', max_length=128, blank=True)),
                ('description', models.TextField(verbose_name='description', max_length=512, blank=True)),
                ('show_in_list', models.BooleanField(verbose_name='show in list', default=True, help_text='Show this person in personnel list plugins.')),
                ('order_no', models.PositiveSmallIntegerField(verbose_name='order number', default=0, help_text='Determines the order in which personnel are shown in. Smallest values first.')),
                ('department', models.ForeignKey(verbose_name='department', on_delete=django.db.models.deletion.SET_NULL, related_name='personnel_in_department', null=True, blank=True, to='cmsplugin_offices_ai.Department')),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True, to='filer.Image')),
                ('office_override', models.ForeignKey(verbose_name='office', on_delete=django.db.models.deletion.SET_NULL, related_name='personnel_in_office', null=True, help_text='Overrides the office the person is assumed to belong to via selected department.', blank=True, to='cmsplugin_offices_ai.Office')),
            ],
            options={
                'verbose_name': 'person',
                'ordering': ['name'],
                'verbose_name_plural': 'personnel',
            },
        ),
        migrations.CreateModel(
            name='PersonnelListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_offices_ai_personnellistplugin', auto_created=True, to='cms.CMSPlugin', parent_link=True, primary_key=True, serialize=False)),
                ('personnel', models.ManyToManyField(verbose_name='personnel', related_name='personnel_list_plugins', to='cmsplugin_offices_ai.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='department',
            name='office',
            field=models.ForeignKey(verbose_name='office', on_delete=django.db.models.deletion.SET_NULL, related_name='departments', null=True, blank=True, to='cmsplugin_offices_ai.Office'),
        ),
        migrations.AddField(
            model_name='contactinformationentry',
            name='department',
            field=models.ForeignKey(verbose_name='department', related_name='department_contact_information', null=True, blank=True, to='cmsplugin_offices_ai.Department'),
        ),
        migrations.AddField(
            model_name='contactinformationentry',
            name='office',
            field=models.ForeignKey(verbose_name='office', related_name='office_contact_information', null=True, blank=True, to='cmsplugin_offices_ai.Office'),
        ),
        migrations.AddField(
            model_name='contactinformationentry',
            name='person',
            field=models.ForeignKey(verbose_name='person', related_name='person_contact_information', null=True, blank=True, to='cmsplugin_offices_ai.Person'),
        ),
    ]
