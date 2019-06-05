#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: auth.py
@time: 2019/06/05
@software: PyCharm
@detail: 用户验证蓝图
"""

from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from albumy.forms.auth import RegisterForm
from albumy.models import User
from albumy.extensions import db
from albumy.utils import generate_token
from albumy.settings import Operations
from albumy.emails import send_confirm_email


def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data.lower()
        username = form.username.data
        password = form.password.data
        user = User(name=name, email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        token = generate_token(user=user, operation=Operations.CONFIRM)
        send_confirm_email(user=user, token=token)
        flash('Confirm email sent, check your inbox.', 'info')
        return redirect(url_for('.login'))
    return render_template('auth/register.html', form=form)
