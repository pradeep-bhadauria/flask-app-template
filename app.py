from flask import Flask
from flask_minify import minify
from flask_assets import Environment, Bundle
from view.home import mod as home

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.register_blueprint(home)
app.config['MINIFY_PAGE'] = True
minify(app=app, html=True, js=True, cssless=True)

assets = Environment(app)
assets.versions = 'timestamp'

app_css = Bundle(
    'vendor/css/bootstrap-4.1.0.min.css',
    'css/main.css',
    filters='cssmin',
    output='main.min.css'
)
app_js = Bundle(
    'vendor/js/jquery-3.3.1.min.js',
    'vendor/js/jquery.validate-1.17.0.min.js',
    'vendor/js/bootstrap-4.1.0.min.js',
    'vendor/js/moment-with-locales-2.18.1.min.js',
    'js/jquery.cookie.js',
    'js/main.js',
    filters='jsmin',
    output='main.min.js'
)
assets.register('app_css', app_css)
assets.register('app_js', app_js)


if __name__ == '__main__':
    app.run()
