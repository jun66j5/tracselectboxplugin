# -*- coding: utf-8 -*-

from pkg_resources import resource_exists, resource_filename

from trac.config import ListOption
from trac.core import Component, implements
from trac.web.api import IRequestFilter
from trac.web.chrome import (ITemplateProvider, add_stylesheet, add_script,
                             add_script_data)


class TracSeelctBoxModule(Component):

    implements(IRequestFilter, ITemplateProvider)

    stylesheets = ListOption(
        'tracselectbox', 'stylesheets', 'tracselectbox/css/select2.css',
        doc='Stylesheets to use instead of default stylesheets')
    htdocs_dir = resource_filename(__name__, 'htdocs')

    # IRequestFilter methods

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        for path in self.stylesheets:
            add_stylesheet(req, path)

        lang = None
        if req.locale:
            lang = str(req.locale).replace('_', '-')
            if not resource_exists(__name__, 'htdocs/js/i18n/%s.js' % lang):
                lang = None
        add_script(req, 'tracselectbox/js/select2.js')
        if lang:
            script_data = {'language': lang}
            add_script_data(req, {'tracselectbox': script_data})
            add_script(req, 'tracselectbox/js/i18n/%s.js' % lang)
        add_script(req, 'tracselectbox/js/main.js')

        return template, data, content_type

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        return [('tracselectbox', self.htdocs_dir)]

    def get_templates_dirs(self):
        return ()
