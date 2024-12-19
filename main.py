import logging
from flask import Flask
from flask_cors import CORS
from routes import routes
from api import apis

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
])

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.register_blueprint(routes)
app.register_blueprint(apis)

if __name__ == "__main__":
    app.run(debug=True)
