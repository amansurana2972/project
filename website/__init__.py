
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path 
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME ="db.db"
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="helloworld"
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
    db.init_app(app)
    app.app_context().push()
  

    from .views import views
    from .auth import auth
    from .models import User
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/" )
    
    
    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    
    return app

        
    
    
 