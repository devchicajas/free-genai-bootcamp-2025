from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'
    
    # Allow all origins
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, support_credentials=True)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import routes after db is initialized
    from lang_portal.app import bp
    app.register_blueprint(bp)
    
    return app 