|PyPI| |PyPI - Status| |Travis (.com)| |Libraries.io dependency status
for latest release| |GitHub|

PACS Workload Generator
=======================

This is a workload generator designed especifically to perform load
testing for several applications. The internal use case of this workload
generator is for load testing AWS Lambda functions, but it can be used
for other purposes. All you have to do is give it a ``worker`` function
and the number of requests per second you want to achieve on average and
it will do the rest for you.

Pypi: https://pypi.org/project/pacswg/

Github Repository: https://github.com/nimamahmoudi/pacswg

Usage
=====

Check out the `examples directory <./examples/>`__.

Installation
============

Install using pip:

.. code:: bash

   $ pip install pacswg

Upgrading:

.. code:: bash

   pip install pacswg --upgrade

For installation in development mode:

::

   git clone https://github.com/nimamahmoudi/pacswg
   cd pacswg
   pip install -e .

.. |PyPI| image:: https://img.shields.io/pypi/v/pacswg.svg
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/pacswg.svg
.. |Travis (.com)| image:: https://img.shields.io/travis/com/nimamahmoudi/pacswg.svg
.. |Libraries.io dependency status for latest release| image:: https://img.shields.io/librariesio/release/pypi/pacswg.svg
.. |GitHub| image:: https://img.shields.io/github/license/nimamahmoudi/pacswg.svg

