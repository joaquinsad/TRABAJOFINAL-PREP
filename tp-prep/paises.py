@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT country_name,region_name From countries as c' 
        'join regions as r on c.region_id = r.region_id'
    ).fetchall()
    return render_template('paises/index.html', posts=posts)