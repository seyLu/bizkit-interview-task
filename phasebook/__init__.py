from flask import Flask

from . import match, search


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def hello() -> str:
        return "Hello World!"

    app.register_blueprint(match.bp)
    app.register_blueprint(search.bp)

    return app
