from flask import Flask, jsonify
from flask_cors import CORS

from google.cloud.logging import Client as LoggingClient

from src.padel_requests import PADEL_REQUESTS, map_date

app = Flask(__name__)
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})
logging_client = LoggingClient()
logging_client.setup_logging()


@app.route("/get_schedule/<provider>/<date>", methods=["GET"])
def get_schedule(provider, date):
    function = PADEL_REQUESTS[provider].get_schedule
    date = map_date(date)
    return jsonify(function(date))


@app.route("/get_availability/<provider>/<resource>/<date>/<hour>", methods=["GET"])
def get_availability(provider, resource, date, hour):
    function = PADEL_REQUESTS[provider].get_availability
    date = map_date(date)
    return jsonify(function(resource, date, hour))


@app.route("/get_fixed_time_info/<provider>/<resource>/<date>/<hour>", methods=["GET"])
def get_fixed_time_info(provider, resource, date, hour):
    function = PADEL_REQUESTS[provider].get_fixed_time_info
    date = map_date(date)
    return jsonify(function(resource, date, hour))


@app.route("/", methods=["GET"])
def index():
    return """
        <p>Go to <a href="/get_schedule/<provider>/<date>">/get_schedule/provider/date</a></p>
    """
