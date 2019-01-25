from flask import Flask, jsonify, request
from api.controllers import Routes
app = Flask(__name__)
get_record = Routes()

@app.route('/', methods=['GET'])
def home():
    return jsonify({
    "message": "Welcome to my app"
  })

@app.route("/v2/incidents", methods = ["GET"])
def get_all_incidents():
    return get_record.fetch_all_incidents()

@app.route("/v2/incidents/<int:record_id>", methods =["GET"])
def get_an_incident(record_id):
    return get_record.fetch_an_incident(record_id)

@app.route("/v2/incidents", methods =["POST"])
def create_an_incident():
    return get_record.insert_incident()

@app.route("/v2/redflags", methods =["POST"])
def create_an_redflag():
    return get_record.insert_redflag()

@app.route("/v2/incidents/<int:record_id>/location", methods =["PATCH"])
def edit_an_incident(record_id):
  request_data = request.get_json()
  location=request_data["location"]
  return get_record.edit_incident(record_id, location)

@app.route("/v2/incidents/<int:record_id>/comment", methods =["PATCH"])
def edit_a_comment(record_id):
  request_data = request.get_json()
  comment = request_data["comment"]
  return get_record.edit_comment(record_id,comment)

@app.route("/v2/incidents/<int:record_id>/status", methods =["PATCH"])
def edit_status_incident(record_id):
  request_data = request.get_json()
  status=request_data["status"]
  return get_record.edit_a_status(record_id,status)

@app.route("/v2/incidents/<int:record_id>/status", methods =["PATCH"])
def edit_status_redflag(record_id):
  request_data = request.get_json()
  status=request_data["status"]
  return get_record.edit_redflag_status(record_id,status)

@app.route("/v2/incidents/<int:record_id>/comment", methods =["PATCH"])
def edit_a_redflag_comment(record_id):
  request_data = request.get_json()
  comment = request_data["comment"]
  return get_record.edit_flag_comment(record_id,comment)