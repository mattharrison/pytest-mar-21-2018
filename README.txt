=====================
 Pytest Introduction
=====================

Copyright 2018 - Matt Harrison

@__mharrison__

http://bit.ly/pytest-mar-21-2018

Assignment 1
============

* Install pytest in a virtual environment
* Run::

    pytest -h


Assignment 2
============

* Create a directory/module ``Integer/integr.py``
  (note spelling).

  * Create a function, ``parse``, that accepts a
    string of the form ``"1,3,5,9"`` that returns
    a list of integers (``[1, 3, 5, 9]``)

* Create a test directory and test file ``Integer/test/test_integr.py``

  * Create a test function, ``test_basic`` that
    asserts that ``integr.parse`` works with the
    input ``"1,3,5,9"``

* Run pytest on ``test/test_integr.py``


Assignment 3
============

* Create a test function, ``test_bad1`` that
  asserts that an error is raised when
  ``integr.parse`` is called with ``'bad input'``.
  Use a context manager (``with``)

* Create a test function, ``test_bad2`` that
  asserts that an error is raised when
  ``integr.parse`` is called with ``'1-3,12-15'``.
  Use the ``@pytest.mark.xfail`` decorator.


Assignment 4
============

* Add a ``__name__`` check that will run pytest
  on ``test/test_integr.py`` if it is executed
  with ``python``

* Run the command line option to collect the tests
  (but not execute them).

* Run only the ``test_basic`` test from the command line.


Assignment 5
============

* Create a doctest on the ``integr.py`` module that
  shows an example of running the ``parse`` function.

* Run the doctest via pytest with a command line option

* Create a ``pytest.ini`` file. Add an option to the
  configuration file to run the doctests when ``pytest``
  is invoked

* Run the doctest via pytest without a command line option



Assignment 6
============

* Run the tests that have ``bad`` in the name

* Mark ``test_bad1`` and ``test_bad2`` with the ``wrong`` name.

* Run only tests that are marked with ``wrong``.

* Run pytest with ``--strict``

* Register ``bad`` as a marker in ``pytest.ini``

* Run pytest with ``--strict``

Assignment 7
============

* Make a new test, ``test_good``, that is parameterized
  to check that ``'1,2,3'`` and ``'9,8,1'`` both work.

* Make a new test, ``test_fail``, that is parameterized
  to check that ``''``, ``None``, and ``[]`` fail.




