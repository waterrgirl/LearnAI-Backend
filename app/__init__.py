# app/__init__.py
import os
from flask import Flask
from flask_cors import CORS
# from pyngrok import ngrok

from app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    # ——— ngrok tunnel (commented out) ———
    # ngrok.set_auth_token("2uarnvaygW75bBBGIEMG3ZOPqB2_ChDfLvvQHhBzoAQpfptp")
    # public_url = ngrok.connect(5001).public_url
    # print(" * ngrok tunnel:", public_url)

    app.register_blueprint(main_blueprint)
    return app

