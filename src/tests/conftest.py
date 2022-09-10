# -*- coding: utf-8 -*-
"""
This script contains the pytest fixture which is available for all the tests.

# @Time : 9/9/2022 4:04 PM
# @Author : rohan.ijare
"""
import pytest

from src.regression_model.config.core import config
from src.regression_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)
