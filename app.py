from api.views import app
from api.dbconnect import Dbconnection

testss = Dbconnection()

if __name__ == "__main__":
	testss.tables()
	testss.table_one()
	testss.table_two()
	app.run(debug = True,port=5009)
