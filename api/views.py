from flask import Flask, jsonify, request
from api.models import Incident, my_red_flags


app = Flask(__name__)

@app.route("/")
def home():
    """A welcoming route to my api"""

    return jsonify({
        'message': "Welcome to Mastula\'s iReporter app.",
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
    

#API end point to fetch a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["GET"])
def get_a_redflag(flag_id):
    red_flag_record= [red_flag for red_flag in my_red_flags if red_flag['id'] == flag_id]
    if red_flag_record:
        return jsonify({
            "status": 200,
        	"redflag": red_flag_record
        	}), 200
    return jsonify({
    	"status": 404,
        "Error": " Invalid record"
    	})

# API end point to delete a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_red_flag(flag_id):
    red_flag_record = [flag for flag in my_red_flags if flag['id'] == flag_id]
    if len(my_red_flags) == 0:
        return jsonify({
        	"status": "400",
            "Error": "Invalid request"
        	}), 404
    my_red_flags.remove(red_flag_record[0])
    return jsonify({
    	'Result': "record was deleted successfully"
    	}), 204




 # API end point to edit location of  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/location", methods=["PUT"])
def edit_red_flag_location(flag_id):
    data = request.get_json()

    for red_flag_record in my_red_flags:
        if red_flag_record['id'] == flag_id:
            red_flag_record["location"] = data["location"]
            return jsonify({
                "status" : 200, 
                "data": [{
                    "id": "flag_id", 
                    "message": "Updated red-flag's record location",
                    "red_flag":red_flag_record
                    }]
            }), 200
    
    
    if not red_flag_record:
        return jsonify({
                         "status": "400",
                        "Error": "Red flag is not available"
                        })

# API end point to edit comment of a  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/comment", methods=["PUT"])
def edit_red_flag_comment(flag_id):
    data = request.get_json()
    for red_flag_record in my_red_flags:
        if red_flag_record['id'] == flag_id:
            red_flag_record["comment"]= data["comment"]
            return jsonify({
                "status" : 200, 
                "data": [{
                    "id": "flag_id",
                    "message": "Updated red-flag's record comment"
                    }]
                }), 200
    if not red_flag_record:
        return jsonify({
                        "status": "400",
                        "Error": "Red flag is not available"
                        })
   