from flask import Flask,jsonify,json,request
from api.dbconnect import Dbconnection
app = Flask(__name__)
new_db = Dbconnection()
class Routes:
    def fetch_all_incidents(self):
        get_record=new_db.get_incident()
        if get_record:
            return jsonify({
                'status': 200,
                'data':get_record
                })
        return jsonify({
            'status':400,
            'Error':"No records found"
            })
    def fetch_an_incident(self,record_id):
        get_record= new_db.get_an_incident(record_id)
        if get_record:
            return jsonify({
                'status':200,
                'data':get_record
            })
        return jsonify({
            'status': 400,
            'Error': "Record not found"
            })
    def insert_incident(self):
        if not request.json:
            return jsonify({
               'status':400,
                'message':'Record not created'
            })
        data = request.get_json()
        if 'createdBy' not in data:
            return jsonify({
               'status':400, 'Error': 'information is missing' 
            })
        createdBy=data["createdBy"] 
        interventiontype=data["interventiontype"]
        location = data["location"]
        status = data["status"]
        comment = data["comment"]
        get_record = new_db.create_incident(createdBy,interventiontype,location,status,comment)  
        return jsonify ({
            'status':200,
            'message':'created intervention record'
        })
    def edit_incident(self,record_id,location):
        get_record =new_db.update_incident(record_id,location)
        if get_record:
            return jsonify({
                'status': 200,
                'id': get_record['record_id'],
                'message':'Update is succesful'
            })
        return jsonify({
            'status':400,
            'message':'Failed to update'
        })
    def edit_comment(self,record_id,comment):
        get_record = new_db.edit_incident(record_id,comment)
        if get_record:
            return jsonify({
                'status':200,
                'id': get_record['record_id'],
                'message':'Update is successful'
            })
        return jsonify({
            'status':400,
            'message':'Failed to update'
        })
    def edit_a_status(self,record_id,status):
        get_record = new_db.edit_status(record_id,status)
        if get_record:
            return jsonify({
                'status':200,
                'id':get_record['record_id'],
                'message':'Update is successful'
            })
        return jsonify({
            'status':400,
            'message':'Failed to update'
        })

    def edit_redflag_status(self,record_id,status):
        get_record = new_db.edit_status_redflag(record_id,status)
        if get_record:
            return jsonify({
                'status':200,
                'id':get_record['record_id'],
                'message':'Update is successful'
            })
        return jsonify({
            'status':400,
            'message':'Failed to update'
        })

    def insert_redflag(self):
        if not request.json:
            return jsonify({
               'status':400,
                'message':'Record not created'
            })
        data = request.get_json()
        if 'createdBy' not in data:
            return jsonify({
               'status':400, 'Error': 'information is missing' 
            })
        createdBy=data["createdBy"] 
        redflagtype=data["redflagtype"]
        location = data["location"]
        status = data["status"]
        comment = data["comment"]
        get_record = new_db.post_redflag(createdBy,redflagtype,location,status,comment)  
        #data.append(get_record.create_incident())  
        return jsonify ({
            'status':200,
            'message':'created intervention record'
        })

    def edit_flag_comment(self,record_id,comment):
        get_record = new_db.edit_redflag_comment(record_id,comment)
        if get_record:
            return jsonify({
                'status':200,
                'id': get_record['record_id'],
                'message':'Update is successful'
            })
        return jsonify({
            'status':400,
            'message':'Failed to update'
        })

    def delete_an_incident(self,record_id):
        get_record = new_db.delete_incident(record_id)
        if get_record:
            return jsonify({
                'status':200,
                'id':get_record['record_id'],
                'message':'Intervention record has been deleted'
            })
        return jsonify({
            'status':200,
            'message':'Failed to delete the record'
        })