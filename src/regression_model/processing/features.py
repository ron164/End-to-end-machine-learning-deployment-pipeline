# -*- coding: utf-8 -*-
"""
# @Time : 9/9/2022 11:24 AM
# @Author : rohan.ijare
"""
from typing import List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTrasnformer(BaseEstimator, TransformerMixin):
    """Temporal elapsed time trasnformer."""

    def __init__(self, variables: List[str], reference_variable: str):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")
        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        """We need this step to fit the sklearn pipeline"""
        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]
        return X


class Mapper(BaseEstimator, TransformerMixin):
    """Categorical variable mapper."""

    def __init__(self, variables: List[str], mappings: dict):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")
        self.variables = variables
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)
        return X
