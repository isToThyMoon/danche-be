from flask import request, jsonify, session, render_template, redirect, url_for, flash, make_response
from flask_login import login_user, logout_user, login_required
from bike.models.base import db
from bike.models.user import User
from bike.models.city import City
from . import web
import json


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = request.get_json()
    print(form)
    if request.method == 'POST':
        with db.auto_commit():
            user = User()
            user.set_attrs(form)
            db.session.add(user)
        return jsonify({'code': 0, 'message': 'success'})


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = request.get_json()
    if request.method == 'POST':
        user = User.query.filter_by(sys_user_name=form['sys_user_name']).first()
        if user and user.check_password(form['password']):

            print('请求初的cookies', request.cookies)
            print('设置login_user前的session', session)
            login_user(user)
            print('设置login_user后的session', session)
            
            return jsonify({'code': 0, 'emp_name': user.cadmin_name})
        return jsonify({'code': 1, 'message': 'not have this cadmin'})
    return ''

@web.route('/loginout')
@login_required
def logout():
    print('退出登录发送的cookie', request.cookies)
    logout_user()
    print('退出登录后的session', session)
    return jsonify({'code': 0, 'message': '退出登录成功！'})
