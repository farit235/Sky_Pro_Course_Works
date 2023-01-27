from flask import Flask
from main.view import main_blueprint
from api.api import api_blueprint
import utils

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix="/")

app.register_blueprint(api_blueprint, url_prefix="/api/")

app.register_error_handler(404, utils.handle_bad_request)

app.register_error_handler(500, utils.internal_error)

app.run()
