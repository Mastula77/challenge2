from api.views import app
from api.dbconnect import Dbconnection

db = Dbconnection()

if __name__ == "__main__":
	app.run(debug = False)
	db.tables()
	db.tables1()
	db.create_users()


	

