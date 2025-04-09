# app.py (at the project root)
from app import create_app

if __name__ == "__main__":
    # Create the Flask app using the factory method
    app = create_app()
    
    # Run the server on host 0.0.0.0 and port 5001
    app.run(host="0.0.0.0", port=5001)
 