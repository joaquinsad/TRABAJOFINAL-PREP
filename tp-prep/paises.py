from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from . import db
bp = Blueprint('paises', __name__)

@bp.route('/paises')
def index():
    d = db.get_db()
    posts = d.execute(
        """SELECT country_name,region_name From countries as c
        join regions as r on c.region_id = r.region_id"""
    ).fetchall()
    return render_template('paises/paises.html', posts=posts)