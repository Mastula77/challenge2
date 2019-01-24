from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

class Dbconnection: 

    def __init__(self):
        self.connection = psycopg2.connect(
            host="127.0.0.1", dbname="challenge3", user="hayirat", password="password"
            )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor=self.connection.cursor(cursor_factory=RealDictCursor)

    def connent_to_db(self):
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("you are connected to -", record, "\n")

    def tables(self):
        create_user = """CREATE TABLE IF NOT EXISTS Users(\
        user_id SERIAL primary key,\
        firstname VARCHAR(20) ,\
        lastname VARCHAR(20) ,\
        username VARCHAR(15) ,\
        othernames VARCHAR(15) ,\
        email VARCHAR(30) NOT NULL,\
        phonenumber VARCHAR(15) ,\
        registered TIMESTAMP ,\
        Is_admin BOOLEAN DEFAULT FALSE,\
        password VARCHAR(20) NOT NULL);"""
        self.cursor.execute(create_user)

    def tables1(self):
        create_record = """CREATE TABLE IF NOT EXISTS Incidents(\
        record_id SERIAL primary key,\
        createdOn TIMESTAMP,\
        createdBy VARCHAR(30) NOT NULL,\
        interventiontype VARCHAR(30) NOT NULL,\
        location VARCHAR(30) NOT NULL,\
        status VARCHAR(30) NOT NULL,\
        image VARCHAR(30),\
        videos VARCHAR(30),\
        comment VARCHAR(50));"""
        
        self.cursor.execute(create_record)
    def get_incident(self):
        select_records = """SELECT * FROM Incidents;"""
        self.cursor.execute(select_records)
        result =self.cursor.fetchall()
        return result
    def get_an_incident(self,record_id):
        select_record = f"""SELECT * FROM Incidents WHERE record_id={record_id};"""
        self.cursor.execute(select_record)
        result = self.cursor.fetchone()
        return result

    def update_incident(self,location, record_id):
        update_record = """ UPDATE Incidents SET location ='{}'\
        WHERE record_id = '{}'""".format(location, record_id)
        self.cursor.execute(update_record)
        result = self.cursor.fetchone()
        return result

    # def create_users(self):

    #     new_user = """INSERT INTO Users(lastname,
    #         username, email, password
    #         ) 
    #         VALUES(
    #         'logose','mercy','logosemastula@gmail.com','12hgan'
    #     );"""
    #     self.cursor.execute(new_user)

    def create_incident(self, createdBy, interventiontype, location,status,comment):
        new_incident = """INSERT INTO Incidents(createdBy, interventiontype, location, status, comment)
        VALUES('{}','{}', '{}', '{}', '{}');""".format(createdBy, interventiontype, location, status, comment)
        self.cursor.execute(new_incident)
        return jsonify({
            'message': 'Incident successfully created'
        })
    #def delete_incident(self)

  