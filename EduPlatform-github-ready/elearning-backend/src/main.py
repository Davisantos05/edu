import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

from .models.user import db
from .routes.user import user_bp
from .routes.courses import courses_bp
from .routes.ebooks import ebooks_bp
from .routes.payments import payments_bp

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

load_dotenv()

def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'unsafe-dev-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'database', 'app.db')}")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(courses_bp, url_prefix='/api')
    app.register_blueprint(ebooks_bp, url_prefix='/api')
    app.register_blueprint(payments_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path and os.path.exists(os.path.join(STATIC_DIR, path)):
            return send_from_directory(STATIC_DIR, path)
        index_path = os.path.join(STATIC_DIR, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(STATIC_DIR, 'index.html')
        return "Frontend não buildado. Rode o frontend separadamente.", 200

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port, debug=True)
