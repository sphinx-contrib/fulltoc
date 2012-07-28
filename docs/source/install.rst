============
 Installing
============

Basic Installation
==================

1. Install the package along with Sphinx.

   There are two ways to install the extension. Using pip::

     $ pip install sphinxcontrib-fulltoc

   or from the source tree::

     $ python setup.py install

2. Add the extension to the list in your ``conf.py`` settings file for
   each project where you want to use it::

      # conf.py
      ...
      extensions = ['sphinxcontrib.fulltoc']
      ...
      
3. Rebuild all of the HTML output for your project.

Advanced Use
============

If you have customized the theme for your documentation, and
especially if you have modified the way sidebars are applied, you may
need to take some additional configuration steps.

localtoc.html
-------------

The ``localtoc.html`` template is used to insert the table of contents
in the sidebar of an HTML page. By default it looks like::

  {%- if display_toc %}
    <h3><a href="{{ pathto(master_doc) }}">{{ _('Table Of Contents') }}</a></h3>
    {{ toc }}
  {%- endif %}

``sphinxcontrib-fulltoc`` forces ``display_toc`` to be set to True and
replaces the ``toc`` variable with the full table of contents. If your
``localtoc.html`` document has been changed, you may need to update it
to include ``{{ toc }}``, or restore the template to the default.

The *Full* Full TOC
-------------------

If you do not want the table of contents collapsed to ignore
subheadings on other pages, you can replace the ``{{ toc }}`` line in
``localtoc.html`` with a call to ``toctree()``, which accepts two
parameters.

.. py:function:: toctree(collapse=True)

   Generate a table of contents relative to the current document.

   :param collapse: Controls whether or not remote parts of the tree
                    are shown. Setting to True only shows internal
                    links on the current page. Setting to False
                    shows internal links on all pages.
   :type collapse: bool
   :return: HTML text of the table of contents

