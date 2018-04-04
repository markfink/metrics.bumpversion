# -*- coding: utf-8 -*-
import os
import tempfile
from shutil import copyfile

import pytest

from metrics_bumpversion.info import BumpversionMetric
from metrics_bumpversion import BUMPVERSION_FILE
from . import here


@pytest.fixture
def tempfolder():
    """setup tempfolder with .metrics file and cd into it."""
    curr_dir = os.getcwd()
    with tempfile.TemporaryDirectory() as temp:
        os.chdir(temp)
        yield
        os.chdir(curr_dir)


@pytest.fixture
def bumpversion_info(tempfolder):
    """Get CovMetric with info loaded from the .coverage file"""
    copyfile(here('resources/' + BUMPVERSION_FILE), BUMPVERSION_FILE)
    return BumpversionMetric({})


def test_bumpversion_metric(bumpversion_info):
    assert bumpversion_info.build_metrics == {'version': '0.0.1'}


def test_bumpversion_metric_no_cfg_file(tempfolder):
    assert BumpversionMetric({}).build_metrics == {}
