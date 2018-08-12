# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 t-kenji.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

import os
from pkg_resources import parse_version, resource_filename
from inspect import getdoc

from trac import __version__ as trac_version
from trac.core import *
from trac.web.api import IRequestFilter
from trac.web.chrome import ITemplateStreamFilter, ITemplateProvider
from genshi.filters.transform import Transformer

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
        return stream

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        return [('nekotheme', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]
