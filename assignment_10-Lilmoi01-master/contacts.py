import json
import os
import sqlite3

class Contacts:

    def __init__(self):
        self.database_name = ""
    
    def set_database_name(self, database_name):
        self.database_name = database_name

        if os.path.exists(self.database_name):
            return 
        else:
            con = sqlite3.connect(self.database_name)
            cur = con.cursor()

            cur.execute(''' CREATE TABLE IF NOT EXISTS contacts (
                contact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL)''')

            cur.execute(''' CREATE TABLE IF NOT EXISTS phones (
                phone_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                contact_id INTEGER NOT NULL,
                phone_type TEXT NOT NULL,
                phone_number TEXT NOT NULL)''')

            con.commit()
            con.close()

    def get_database_name(self):
        return self.database_name()

    def add_contact(self, first_name, last_name):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()

        cur.execute(''' INSERT INTO contacts (first_name, last_name) VALUES (?,?)''', (first_name, last_name))

        con.commit()
        con.close()

    def modify_contact(self, contact_id, first_name, last_name):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()

        cur.execute(''' UPDATE contacts SET first_name = ?, last_name = ? WHERE contact_id = ?''', 
        (first_name, last_name, contact_id))
        con.commit()
        con.close()

    def add_phone(self, contact_id, phone_type, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute(''' INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?,?,?)''', 
        (contact_id, phone_type, phone_number))
        con.commit()
        con.close()

    def modify_phone(self, phone_id, phone_type, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute(''' UPDATE phones SET phone_type = ?, phone_number = ? WHERE phone_id = ?''', 
        (phone_type, phone_number, phone_id))
        con.commit()
        con.close()

    def get_contact_phone_list(self):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id ''')
        temp = cur.fetchall()
        con.commit()
        con.close()

        return temp