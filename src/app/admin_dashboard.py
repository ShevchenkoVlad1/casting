# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        # append an app list module for "Casting"
        self.children.append(modules.ModelList(
            _('Casting'),
            exclude=('auth.*',),
            models=('casting.*',),
            column=0,
            order=1
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            models=('auth.*',),
            column=0,
            order=0
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            10,
            column=2,
            order=1
        ))
