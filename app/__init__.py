from flask import Flask

from . config import Config 
from . extenstions import db,login_manager
from .home.routes import home_bp
from .auth.routes import auth_bp
from .auth.models import User
from .admin import admin_bp



def  create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp,url_prefix="/auth")
    

    app.register_blueprint(admin_bp, url_prefix="/admin")
    
    
    
    return app

    
    
    
    


