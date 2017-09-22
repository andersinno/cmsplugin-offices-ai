====================
cmsplugin-offices-ai
====================

Office, department, and personnel manager for Django CMS.

This CMS app provides a way to manage offices, departments and personnel.


Getting started
---------------

1. Install
2. Add ``'cmsplugin_offices_ai'`` to ``INSTALLED_APPS``
3. Implement frontend
    - This package includes only reference templates in (``templates/cmsplugin_offices_ai/``).
    - This package does not include any styling.


Configuration
-------------

**Google Maps**

Set ``GOOGLE_MAPS_API_KEY`` in Django project settings to show map embed with offices.


Installing for development
--------------------------

Use ``pip install -e /path/to/checkout`` to install as "editable" package to your venv
