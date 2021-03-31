from flask import Flask, request, jsonify
import datetime
import psycopg2
from psycopg2 import sql
import rds_config

# initiate flask API
app = Flask(__name__)

# load all the DB configs from rds_configs.py file
rds_host = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
table_name = rds_config.db_table_name

# create a connection to the DB
conn = psycopg2.connect(dbname=db_name, user=name, password=password, host=rds_host)
cur = conn.cursor()


# define endpoint path and method
@app.route('/app', methods=["POST"])
def insert_timestamp():
    # create a new datetime object
    dt = datetime.datetime.now()

    # insert it to the DB
    cur.execute(sql.SQL("INSERT INTO {} (timestamp) VALUES (%s)").format(sql.Identifier(table_name)), (dt,))
    # commit the data
    conn.commit()

    # return successful response
    return {}, 200


# main method to run the server
if __name__ == '__main__':
    # run the server in the given port
    app.run(port=rds_config.api_port)
