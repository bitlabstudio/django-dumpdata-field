Django Dumpdata Field
============

custom dumpdata and loaddata commands that allow to export given fields of a model

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-dumpdata-field

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-dumpdata-field.git#egg=dumpdata_field

TODO: Describe further installation steps (edit / remove the examples below):

Add ``dumpdata_field`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'dumpdata_field',
    )

Add the ``dumpdata_field`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^/', include('dumpdata_field.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load dumpdata_field_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate dumpdata_field


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-dumpdata-field
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
