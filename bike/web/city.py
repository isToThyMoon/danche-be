from flask import request, jsonify, session, render_template, redirect, url_for, flash, make_response
from bike.models.base import db
from bike.models.city import City
from . import web
import json


@web.route('/city/open', methods=['GET', 'POST'])
def open_city():
    form = request.get_json()
    print(form)
    if request.method == 'POST':
        with db.auto_commit():
            city = City()
            city.set_attrs(form)
            db.session.add(city)
        return jsonify({'code': 0, 'message': 'success'})


@web.route('/city/filter', methods=['GET', 'POST'])
def city_filter():
    form = request.get_json()
    print('查询关键字', form)
    if request.method == 'POST':
        city = City.query.filter_by(city_name=form['city_name'][1]).first()

        if city:
            res = {'code': 0,
                   'result': {
                       'item_List': [
                           city.to_json()
                       ]
                   }}
            return jsonify(res)