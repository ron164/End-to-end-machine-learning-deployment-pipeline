# -*- coding: utf-8 -*-
"""
# @Time : 8/15/2022 12:06 AM
# @Author : rohan.ijare
"""
import logging

from regression_model.config.core import PACKAGE_ROOT, config

logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())

with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()
