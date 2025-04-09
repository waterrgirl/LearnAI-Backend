# app/__init__.py
from flask import Flask
from flask_cors import CORS
from pyngrok import ngrok

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    
    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Set your ngrok authtoken (keep it secure in real projects)
    ngrok.set_auth_token("2uarnvaygW75bBBGIEMG3ZOPqB2_ChDfLvvQHhBzoAQpfptp")
    
    # Open a public URL for the Flask server on port 5001
    public_url = ngrok.connect(5001).public_url
    print(f"Public URL: {public_url}")

    # Import and register the blueprint containing your routes
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
