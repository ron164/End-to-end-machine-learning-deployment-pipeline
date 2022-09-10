# -*- coding: utf-8 -*-
"""
# @Time : 9/9/2022 4:05 PM
# @Author : rohan.ijare
"""
from src.regression_model.config.core import config
from src.regression_model.processing.features import TemporalVariableTrasnformer


def test_temporal_variable_transformer(sample_input_data):
    transformer = TemporalVariableTrasnformer(
        variables=config.model_config.temporal_vars,
        reference_variable=config.model_config.ref_var,
    )
    assert sample_input_data["YearRemodAdd"].iat[0] == 1961

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["YearRemodAdd"].iat[0] == 49
