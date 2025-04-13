# app.py
import os
from app import create_app

# from pyngrok import ngrok

app = create_app()

# ——— ngrok setup (commented out) ———
# ngrok.set_auth_token("2uarnvaygW75bBBGIEMG3ZOPqB2_ChDfLvvQHhBzoAQpfptp")
# public_url = ngrok.connect(5001).public_url
# print(f"Public URL: {public_url}")

if __name__ == "__main__":
    # Allow overriding port via ENV (e.g. for Cloud Run)
    port = int(os.environ.get("PORT", 5001))
    # debug=True gives you full tracebacks in your terminal
    app.run(host="0.0.0.0", port=port, debug=True)
