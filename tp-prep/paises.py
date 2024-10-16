from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/paises')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT country_name,region_name From countries as c' 
        'join regions as r on c.region_id = r.region_id'
    ).fetchall()
    return render_template('paises/index.html', posts=posts)