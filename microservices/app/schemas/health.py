# -*- coding: utf-8 -*-
"""
# @Time : 9/10/2022 11:20 AM
# @Author : rohan.ijare
"""
from pydantic import BaseModel
from typing import Optional


class Health(BaseModel):
    name: str
    api_version: Optional[str]
    model_version: str
