#!/usr/bin/python3
""" Import models"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class"""
    state_id = ""
    name = ""
