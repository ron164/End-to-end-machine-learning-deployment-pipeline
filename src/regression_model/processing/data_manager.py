# -*- coding: utf-8 -*-
"""
# @Time : 9/9/2022 2:06 PM
# @Author : rohan.ijare
"""
import typing as t
from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from regression_model import __version__ as _version
from regression_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))
    dataframe["MSSubClass"] = dataframe["MSSubClass"].astype("O")

    # rename variables beginning with numbers to avoid syntax errors later
    transformed = dataframe.rename(columns=config.model_config.variables_to_rename)
    return transformed


def remove_old_pipelines(*, files_to_keep: t.List[str]):
    """Automatically removes the old version, this is to ensure that is correct
    traceability between package and model version."""
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()


def save_pipeline(*, pipeline: Pipeline) -> None:
    """Continue the pipeline
    Save the versioned model, and overwrite any previous saved models.
    This ensures that only one trained model is called when published and can be traced."""
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name
    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load the pipeline"""
    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model
