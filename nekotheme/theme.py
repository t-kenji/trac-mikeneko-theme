# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 t-kenji.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

from pkg_resources import parse_version, resource_filename

from trac import __version__ as trac_version
from trac.core import *
from trac.web.chrome import ITemplateStreamFilter, ITemplateProvider
from genshi.filters.transform import Transformer

from themeengine.api import ThemeBase


class TracMikenekoTheme(ThemeBase):

    implements(ITemplateProvider)

    htdocs = True
    screenshot = True
    template = True

    # ITemplateProvider methods 

    def get_htdocs_dirs(self):
        return [('nekotheme', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]
