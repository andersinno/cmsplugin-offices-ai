# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='cmsplugin-offices-ai',
    version='0.0.0',
    author='Anders Innovations',
    author_email='info@anders.fi',
    packages=find_packages(
        exclude=[
            "tests",
        ],
    ),
    include_package_data=True,
    license='MIT',
    long_description=open('README.md').read(),
    description='Office and personnel management app for Django CMS',
    install_requires=[
        'django-cms>=3.2,<3.5',
        'django-filer>=1.2.4',
        'django-enumfields>=0.9.0',
        'easy-thumbnails>=2.3',
    ],
    url='https://github.com/andersinno/cmsplugin-offices-ai',
)
