# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 t-kenji.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

import os
import itertools
from pkg_resources import parse_version, resource_filename
from inspect import getdoc

from trac import __version__ as trac_version
from trac.core import *
from trac.web.chrome import ITemplateStreamFilter, ITemplateProvider
from genshi.builder import tag
from genshi.filters.transform import Transformer, START

from themeengine.api import ThemeBase, IThemeProvider


class TracMikenekoTheme(ThemeBase):

    implements(ITemplateStreamFilter, ITemplateProvider)

    first_name = 'mikeneko'

    # IThemeProvider

    def get_theme_names(self):
        yield self.first_name + '_mike'
        yield self.first_name + '_coco'

    def get_template_overrides(self, name):
        return ()

    def get_theme_info(self, name):
        name = name.split('_')
        if name[0] != self.first_name:
            raise TracError('Internal Error')
        return {
            'description': getdoc(self.__class__),
            'screenshot': 'htdocs/screenshot_{name}.png'.format(name=name[1]),
            'template': os.path.join('templates', '{name}_theme.html'.format(name=name[1])),
            'htdocs': 'htdocs',
            'css': 'css/{name}.css'.format(name=name[1]),
            'scripts': [
                ('theme/js/{name}.js'.format(name=name[1]),),
            ],
        }

    # ITemplateStreamFilter methods

    def filter_stream(self, req, method, filename, stream, data):
        if not req.path_info.startswith('/ticket'):
            return stream

        def _find_change(stream):
            kind0, data0, pos0 = stream[0]
            class0 = data0[1].get('class', '')

            for kind, data, pos in stream:
                if (kind is START) and (data[1].get('class', '') == 'trac-author-user'):
                    self.env.log.info('data: {}'.format(data0))
                    return itertools.chain([(kind0,
                                            (data0[0], data0[1] | [('class', class0 + ' own')]),
                                             pos0)], stream[1:])
            return stream

        xpath = '//div[@id="changelog"]/div'
        stream |= Transformer(xpath).filter(_find_change)
        return stream

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        return [('nekotheme', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]
