================
 For Developers
================

If you would like to contribute to sphinxcontrib-fulltoc, these
instructions should help you get started.  Patches, bug reports, and
feature requests are all welcome through the `GitHub site
<http://github.com/dreamhost/sphinxcontrib-fulltoc/>`_.  Contributions
in the form of patches or pull requests are easier to integrate and
will receive priority attention.

Building Documentation
======================

The documentation for sphinxcontrib-fulltoc is written in
reStructuredText and converted to HTML using Sphinx, as you might
expect. The build itself is driven by setuptools. You will need the
following packages in order to build the docs:

- Sphinx
- docutils
- sphinxcontrib-fulltoc

Once all of the tools are installed into a virtualenv using pip, run
``python setup.py build_sphinx`` to generate the HTML version of the
documentation::

    $ python setup.py build_sphinx
    
The output version of the documentation ends up in
``./build/sphinx/html`` inside your sandbox.
