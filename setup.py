#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 t-kenji.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

import os
from setuptools import setup

__version__ = '0.2'

setup(
    name = 'TracMikenekoTheme',
    version = __version__,
    description = 'Mikeneko theme for Trac and ThemeEnginePlugin.',
    url = 'https://github.com/t-kenji/trac-mikeneko-theme',
    keywords = 'trac plugin theme',
    classifiers = ['Framework :: Trac'],

    author = 't-kenji',
    author_email = 'protect.2501@gmail.com',
    license = 'BSD',  # the same as Trac
    maintainer='t-kenji',
    maintainer_email='protect.2501@gmail.com',

    packages = ['nekotheme'],
    package_data = {
        'nekotheme': [
            'templates/*.html',
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'htdocs/fonts/*.*',
            'htdocs/*.png',
        ]},
    install_requires = ['TracThemeEngine'],
    entry_points = {
        'trac.plugins': [
            'nekotheme.theme = nekotheme.theme',
        ]
    },
)
