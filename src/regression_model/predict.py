# -*- coding: utf-8 -*-
"""
# @Time : 9/9/2022 3:45 PM
# @Author : rohan.ijare
"""
import typing as t

import numpy as np
import pandas as pd

from src.regression_model import __version__ as _version
from src.regression_model.config.core import config
from src.regression_model.processing.data_manager import load_pipeline
from src.regression_model.processing.validation import validate_input

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    """make a prediction using a saved model pipeline"""
    data = pd.DataFrame(input_data)
    validated_data, errors = validate_input(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}
    if not errors:
        predictions = _price_pipe.predict(X=validated_data[config.model_config.features])
        results = {
            "predictions": [np.exp(pred) for pred in predictions],
            "version": _version,
            "errors": errors
        }
    return results
