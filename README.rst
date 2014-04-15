Django Dumpdata Field
=====================

Custom dumpdata and loaddata commands that allow to export given fields of a
model.

I know this is a really stupid usecase and no one should actually do this, but
let's say you have a staging server where your authors create articles and
maintain the content.

Then you have a production server and when you deploy the site, you actually
export the database of the staging server and import it on the production
server.

That's all good and easy until you have some apps that generate data, for
example click statistics for links and files. You don't want to lose these
stats when you import the database from the staging server.

This app aims to solve that issue.

1. On production: ``./manage.py dumpdata_field app_name.ModelName fields=field1,field2 > output.json``
2. Export the staging database and import it on the produciton server
3. On production: ``./manage.py loaddata_field output.json``

The loaddata command will iterate over all items in the JSON file and see if
that PK still exists on the server. If so, it will load the object and ONLY
change the given field and save the object.

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

Usage
-----

It's quite simple. First export your data like so:

.. code-block:: bash

    ./manage.py dumpdata_field app_name.ModelName fields=field1,field2,field3 > output.json

Then import your data like so:

.. code-block:: bash

    ./manage.py loaddata_field > output.json

Warning: If for some reason a primary key on staging was re-used, this app will
of course not know about this. It will find the PK in the output file, load the
object from the database and update the given fields. If this object is now
a completely different object than it was before on the production server,
you are out of luck. You have been warned.


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
