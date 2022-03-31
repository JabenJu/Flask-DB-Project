from flask import Flask,render_template,request,redirect,url_for
import psycopg2


def get_db_connection():
   conn = psycopg2.connect(
   host = 'localhost',
   database = 'flask_db',
   user = 'postgres',
   password = 'jaben1215'
   )

   return conn

conn = get_db_connection()
curr = conn.cursor()

in_user = "cringe"
in_pass = "cringe"

curr.execute("SELECT username, password FROM users")
records = curr.fetchall()

print(records)
# if [in_user, in_pass] not in users_list:
#     print("Okay")

curr.close()
conn.close()
