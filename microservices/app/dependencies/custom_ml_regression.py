# -*- coding: utf-8 -*-
"""
# @Time : 9/10/2022 10:55 AM
# @Author : rohan.ijare
"""
import os
import sys
sys.path.insert(0, "app")
import json
from typing import Any
import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from regression_model import __version__ as model_version
from regression_model.predict import make_prediction
from schemas.health import Health
from schemas.predict import PredictionResults, MultipleHouseDataInputs
from utils.config import settings
import warnings

warnings.filterwarnings("ignore")

api_router = APIRouter()


@api_router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = Health(
        name=settings.PROJECT_NAME, model_version=model_version
    )

    return health.dict()


@api_router.post("/predict", response_model=PredictionResults, status_code=200)
async def predict(input_data: MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the TID regression model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
