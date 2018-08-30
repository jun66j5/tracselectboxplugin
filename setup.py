#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

kwargs = {
    'name': 'TracSelectBox',
    'version': '0.0.1',
    'description': 'Replace select boxes in Trac',
    'license': 'BSD',  # the same as Trac
    'url': 'https://trac-hacks.org/wiki/TracSelectBoxPlugin',
    'author': 'Jun Omae',
    'author_email': 'jun66j5@gmail.com',
    'install_requires': ['Trac'],
    'packages': setuptools.find_packages(exclude=['*.tests*']),
    'package_data': {
        'tracselectbox': [
            'htdocs/css/*.*',
            'htdocs/js/*.*',
            'htdocs/js/i18n/*.*',
        ],
    },
    'entry_points': {
        'trac.plugins': [
            'tracselectbox.web_ui = tracselectbox.web_ui',
        ],
    },
}

if __name__ == '__main__':
    setuptools.setup(**kwargs)
