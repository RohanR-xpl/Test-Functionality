import os
from flask import Flask
from extensions import db
from blueprints.test_success import test_success_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://openpg:openpgpwd@localhost:5432/zhap_parser_test" 
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(test_success_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
