from datetime import datetime

class Incident:
    
    def __init__(self, createdBy, interventiontype, location, status, Images, Videos, comment):

        self.createdOn = datetime.now()
        self.createdBy = createdBy
        self.interventiontype = interventiontype
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment


class User:

    def __init__(self, firstname, lastname, othernames, email, phone_number, username, registered, is_admin):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.registered = registered
        self.is_admin = is_admin


    