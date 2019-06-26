from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return '404', 404


from bike.web import auth
from bike.web import city