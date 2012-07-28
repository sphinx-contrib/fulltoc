# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Doug Hellmann <doug.hellmann@dreamhost.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from docutils import nodes
from sphinx import addnodes
from sphinx.util.console import red, brown, darkgreen


def builder_inited(app):
    app.info(red('initializing sphinxcontrib-fulltoc'))


def html_page_context(app, pagename, templatename, context, doctree):
    if pagename in app.env.tocs:
        app.builder.info('replacing toc for %s' % pagename)
        # toc = app.env.tocs[pagename].deepcopy()
        # page_toc = app.builder.render_partial(toc)['fragment']
        # context['local_toc'] = page_toc
        # context['toc'] = page_toc
        env = app.env
        fulltoc = env.fulltoc_toctree.deepcopy()
        #print '\n', fulltoc
        env.resolve_references(fulltoc, pagename, app.builder)
        rendered_toc = app.builder.render_partial(fulltoc)['fragment']
        #print 'RENDERED: %r' % rendered_toc
        context['toc'] = rendered_toc
        context['display_toc'] = True  # force toctree to display


def build_full_toctree(builder, docname, tree):
    """Return a single toctree starting from docname containing all
    sub-document doctrees.
    """
    new_toctree = builder.env.get_toctree_for(docname,
                                              builder,
                                              collapse=False,
                                              #maxdepth=1,
                                              #titles_only=True,
                                              )

    for toctreenode in tree.traverse(addnodes.toctree):
        includefiles = map(str, toctreenode['includefiles'])
        for includefile in includefiles:
            try:
                subtree = build_full_toctree(
                    builder,
                    includefile,
                    builder.env.get_doctree(includefile),
                    )
                subtree = builder.env.resolve_toctree(
                    includefile,
                    builder,
                    subtree,
                    )
            except Exception as err:
                #raise
                builder.warn('%r' % err)
                builder.warn('toctree contains ref to nonexisting '
                             'file %r' % includefile,
                             builder.env.doc2path(docname))
            else:
                #sof = addnodes.start_of_file(docname=includefile)
                #sof.children = subtree.children
                #print; print sof
                #new_toctree.append(sof)
                new_toctree.append(subtree)
    return new_toctree


def env_updated(app, env):
    master_doctree = env.get_doctree(env.config.master_doc)
    toctree = build_full_toctree(app.builder,
                                 env.config.master_doc,
                                 master_doctree,
                                 )
    env.fulltoc_toctree = toctree
    # for node in toctree.traverse():
    #     print node.document


def setup(app):
    app.connect('builder-inited', builder_inited)
    app.connect('html-page-context', html_page_context)
    app.connect('env-updated', env_updated)
