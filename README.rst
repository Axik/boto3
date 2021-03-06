=====
boto3
=====

|Build Status|

An evolution of boto, supporting both Python 2 & 3.

This is not a port of boto_, but a ground-up rewrite. We hope to improve on boto
in both consistency & maintainability.

You can find a current version of the documentation on `Read the Docs`_.

**WARNING**: This repo is unstable & the API **WILL** shift as time goes
on. This code is **NOT** yet production-ready.

.. _boto: https://docs.pythonboto.org/
.. _`Read the Docs`: https://boto3.readthedocs.org/en/latest/
.. |Build Status| image:: https://travis-ci.org/boto/boto3.png?branch=develop
   :target: https://travis-ci.org/boto/boto3

Requirements
============

* Python 3.3+ first, but also works on Python 2.6+
* botocore==0.24.0
* six>=1.4.0
* jmespath==0.1.0
* python-dateutil>=2.1


Current Status
==============

Complete
--------

* Low-level ``Connection`` objects are relatively complete, but are usable
  *now*.

    * These are equivalent to the low-level ``*Connection`` objects in boto.
    * Relatively finalized, though they may eventually move down to botocore_
      (still importable & usable in ``boto3`` though).

.. _botocore: https://github.com/boto/botocore

In-progress
-----------

* ``Resource`` objects

    * A more Pythonic/object-y layer on top of the ``Connection`` objects
    * Easier/more natural to work with
    * Basic calls function, but you need to supply all parameters the right way
      (leaning on the API docs a lot) & the responses are pretty raw

* ``Collection`` objects

    * Abstracts working with collections of ``Resource`` objects
    * Basic functionality works (creates/gets data)
    * Processing list data (``.all(...)``)


Running Tests
=============

Setup
-----

Setup looks like::

    $ virtualenv -p python3 env3
    $ . env3/bin/activate
    $ pip install -r requirements.txt
    $ pip install nose

Running Unit Tests
------------------

Running tests looks like::

    $ nosetests -s -v unit

``boto3`` is in a state of flux, so while we strive for passing unit tests &
good test coverage (currently 98%), there may be periods where some failures
are present. This should no longer be the case once we reach beta.

Running Integration Tests
-------------------------

Running **integration** tests (against AWS itself) looks like::

    $ nosetests -s -v integration

**WARNING:** Running integration tests requires a valid AWS account & **WILL**
result in charges to that account based on usage.
