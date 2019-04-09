from flask import Flask, render_template,request
from ext import db, login_manager, bcrypt
from flaskblog.apps.admin.routes import bp as admin_bp
from .routes import bp as front_bp
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
app.register_blueprint(admin_bp)
app.register_blueprint(front_bp)


login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# from flaskblog import routes

@app.errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/admin'):
        return render_template('admin/404.html'), 404
    return '<h1>Page Not Found</h1>', 404
