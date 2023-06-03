from flask import Flask, render_template, send_from_directory
from .extensions import db, bcrypt, cors
from .views import app as main
from .settings import is_production
import os

app = Flask(__name__)

app.config.from_pyfile('settings/production.py' if is_production() else 'settings/development.py')

db.init_app(app)
bcrypt.init_app(app)
cors.init_app(app)

app.register_blueprint(main, url_prefix='')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html.j2', title='404 Error'), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()
