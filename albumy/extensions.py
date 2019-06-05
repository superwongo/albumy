#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: extensions.py
@time: 2019/06/04
@software: PyCharm
@detail: 扩展
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
