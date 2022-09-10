# -*- coding: utf-8 -*-
"""
# @Time : 9/10/2022 12:16 PM
# @Author : rohan.ijare
"""

import os
with open(os.path.join(os.getcwd(), "VERSION")) as version_file:
    __version__ = version_file.read().strip()