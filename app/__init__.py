# app/__init__.py
from flask import Flask
from flask_cors import CORS
from pyngrok import ngrok

def create_app():
    app = Flask(__name__)
    CORS(app)

    # (Optional) Set up ngrok to expose your local server publicly
    from pyngrok import ngrok
    ngrok.set_auth_token("your_ngrok_authtoken_here")
    public_url = ngrok.connect(5001).public_url
    print(f"Public URL: {public_url}")

    # Register the blueprint containing all route definitions
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
