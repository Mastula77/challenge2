from flask import Flask
import psycopg2
from pprint import pprint
from psycopg2 import Error
from psycopg2.extras import RealDictCursor

class Dbconnection: 

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="127.0.0.1", dbname="challenge3", user="hayirat", password="password"
                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor=self.connection.cursor(cursor_factory=RealDictCursor)

        except: 
            pprint("failed to connect to the database")

    def connent_to_db(self):
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("you are connected to -", record, "\n")



    def tables(self):
        try:
            create_user = """CREATE TABLE Users(\
            user_id SERIAL primary key,\
            firstname VARCHAR(20) NOT NULL,\
            lastname VARCHAR(20) NOT NULL,\
            username VARCHAR(15) NOT NULL,\
            othernames VARCHAR(15) NOT NULL,\
            email VARCHAR(30) NOT NULL,\
            phonenumber VARCHAR(15) NOT NULL,\
            registered TIMESTAMP NOT NULL,\
            Is_admin BOOLEAN NOT NULL,\
            password VARCHAR(20) NOT NULL);"""
            self.cursor.execute(create_user)

        except Exception as e:
            pprint(e)

    def tables1(self):
        try:
            create_record = """CREATE TABLE IF NOT EXISTS Incident(\
            record_id SERIAL primary key,\
            createdOn VARCHAR(15) NOT NULL,\
            createdBy VARCHAR(30) NOT NULL,\
            type VARCHAR(30) NOT NULL,\
            location VARCHAR(30) NOT NULL,\
            status VARCHAR(30) NOT NULL,\
            image VARCHAR(30),\
            videos VARCHAR(30),\
            comment VARCHAR(50));"""
            
            self.cursor.execute(create_record)
        except Exception as e:
            pprint(e)


if __name__=='__main__':
    con = Dbconnection()
    con.tables()
    con.tables1()