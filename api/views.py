from flask import Flask, jsonify, request
from api.models import Incident, my_red_flags


app = Flask(__name__)

@app.route("/")
def home():
    """A welcoming route to my api"""

    return jsonify({
        'message': 'Welcome to Mastula\'s iReporter app.',
        'status': '200'
    }), 200

#API end point to create a red-flag record
@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
    if not request.json:#request has no json data
        return jsonify({
            "Error": "There is no data returned from the request",
            "status": 400
            }), 400
    data = request.get_json()
    if 'createdBy' not in data:
        return jsonify({'status': 400, 'Error': 'The information is missing'}), 400

    red_flag = Incident(
    		data["createdBy"], data["type"],
        	data["location"], data["status"], data["Images"],
        	data["Videos"], data["comment"]
       	   )
    my_red_flags.append(
    	red_flag.get_record()
    	)
    return jsonify({
    	"status": 201,
    	"data": [{ 
        "id": red_flag._id,
        "Message": "Created red-flag record"
        }]}), 201



#API end point to fetch all records
@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_red_flags():
    return jsonify({
        "status": 200,
        "data": my_red_flags
        }), 200
    

