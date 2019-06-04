#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: __init__.py.py
@time: 2019/06/04
@software: PyCharm
@detail: 
"""

import os

from flask import Flask

from albumy.settings import config
from albumy.extensions import register_extensions


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('albumy')
    app.config.from_object(config[config_name])

    register_extensions(app)

    return app
