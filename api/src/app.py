from flask import Flask
from flask_cors import CORS

from src.padel_requests import PADEL_REQUESTS

app = Flask(__name__)
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})



@app.route("/get_schedule/<provider>/<date>", methods=["GET"])
def get_schedule(provider, date):
    function = PADEL_REQUESTS[provider]
    return function(date)

@app.route("/", methods=["GET"])
def index():
    return """
        <p>Go to <a href="/get_schedule/<provider>/<date>"></a></p>
    """