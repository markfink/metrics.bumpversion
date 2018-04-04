# -*- coding: utf-8 -*-
"""A metrics plugin to do get version information from .bumpversion.cfg file."""
from __future__ import unicode_literals, print_function
import configparser

from metrics.metricbase import MetricBase

from . import BUMPVERSION_FILE


def get_file_processors():
    """plugin mechanism for file based metrics."""
    return []


def get_build_processors():
    """plugin mechanism for build metrics."""
    return [BumpversionMetric]


class BumpversionMetric(MetricBase):
    """Read the version from the .bumpversion.cfg file."""
    def __init__(self, context):
        self._context = context
        self.reset()

    def reset(self):
        #self._version = None
        config = configparser.ConfigParser()
        config.read(BUMPVERSION_FILE)
        try:
            self._version = config['bumpversion']['current_version']
        except KeyError:
            self._version = None

    def get_build_metrics(self):
        if self._version:
            return {'version': self._version}
        else:
            return {}

    build_metrics = property(get_build_metrics)
