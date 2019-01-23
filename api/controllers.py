from flask import Flask
from api.views import Routes
route_response = Routes()
app = Flask(__name__)

@app.route('/v2/users/signup/', methods = ['POST'])
def post_user():
    return route_response.create_user()


@app.route("/v2/users/login/", methods = ["POST"])
def login_user():
    return route_response.login()



@app.route("/v2/users/", methods = ["GET"])
def get_an_incident():
    return route_response.fetch_an_incident()

@app.route("/v2/users/", methods = ["GET"])
def get_all_incidents():
    return route_response.fetch_all_incidents()

@app.route("/v2/users/<int incident_id>/location", methods = ["PATCH"])
def edit_user():
    return route_response.update_user()


@app.route("/v2/users/<int:incident_id>/", methods = ["DELETE"])
def delete_incident():
    return route_response.delete.record()





