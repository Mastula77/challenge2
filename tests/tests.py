import unittest
import json
from api.views import app, my_red_flags


class BaseTest(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()


		self.sample_record_data = {
            "createdBy": "Mastula",
            "type": "red-flag",
            "location": "Makindye",
            "status": "resolved",
            "Images": "fjh.png",
            "Videos": "ghfg.mp4",
            "comment": "This is good"
            }

class TestRedFlag(BaseTest):
	def test_create_red_flag(self):
		response = self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json"
			)
		
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.content_type, "application/json")
		self.assertIn(b"Created red-flag record", response.data)
		
	#def test_home(self):
		#response = self.client.get('/')
		#assert "Welcome to Mastula\'s iReporter app." in response.data
		#assert response.status_code == 200


	def test_get_all_redflags(self):
		self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json"
			)
		response = self.client.get(
			"/api/v1/red-flags",
			content_type = "application/json"
			)
		self.assertEqual(response.status_code, 200)
		self.assertIn("createdBy", str(response.data))
		self.assertEqual(response.content_type, "application/json")


	""" missing value field = bad """
	def test_post(self):
		record = {
            "type": "",
            "location": "",
            "status": "",
            "Images": "fed.png",
            "Videos": "gfgg.mp4",
            "comment": "" 
			 }
		response = self.client.post(
			"/api/v1/red-flags",
			data=json.dumps(record),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, 400)


	def test_fetch_specific_redflag(self):
		response = self.client.get(
			'/api/v1/red-flags/2',
			content_type = "application/json")
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(response.status_code, 200)


	def test_edit_location(self):
		
		new_location = {"location": "Mukono"}
		response = self.client.put(
			"/api/v1/red-flags/{}/location".format(my_red_flags[0]["id"]),
			content_type="application/json",
			data=json.dumps(new_location)
			)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(my_red_flags[0]["location"], "Mukono")


	def test_edit_comment(self):
		self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json"
			)
		response = self.client.get(
			'/api/v1/red-flags/1',
			content_type = "application/json")
		new_comment = {"comment": "Tribalism"}
		red_flag = json.loads(response.data.decode())["redflag"][0]
		response = self.client.put(
			"/api/v1/red-flags/{}/comment"
			.format(red_flag["id"]),
			content_type="application/json",
			
			data=json.dumps(new_comment)
			)
		self.assertEqual(response.status_code, 200)




	def test_delete_record(self):
		response = self.client.delete(
			"/api/v1/red-flags/1"
			)
		self.assertEqual(response.status_code, 204)
		record ={}
		response = self.client.delete("/api/v1/red-flags/1",
		content_type = "application/json",
		data =json.dumps(record))
		self.assertEqual(len(my_red_flags), 0)

	def test_delete_reecord_which_redflag_id_does_not_exist(self):
		response = self.client.delete("/api/v1/red-flags/21",content_type = "application/json")
		self.assertEqual(response.status_code, 404)


	def test_edit_mycomment(self):
		
		new_comment = {"comment": "Bad reports"}
		response = self.client.put(
			"/api/v1/red-flags/{}/comment".format(my_red_flags[0]["id"]),
			content_type="application/json",
			data=json.dumps(new_comment)
			)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(my_red_flags[0]["comment"], "Bad reports")
