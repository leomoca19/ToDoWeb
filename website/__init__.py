from flask import Flask

def create_app():
    app = Flask()
    app.config['SECRET_KEY'] = 'pythons are scary'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
