#!/usr/bin/python3
"""Test to check output of storage.all()"""
from models import storage
import os


db = os.getenv('HBNB_MYSQL_DB')

print(storage.all("State"))
