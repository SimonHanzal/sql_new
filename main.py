
import mysql.connector as sql

conn = sql.connect(
  host="localhost",
  user="hanza",
  password="matoro370",
  database="sql_test"
)

import sqlite3
import pandas as pd

data = pd.read_csv("covid_impact_on_airport_traffic.csv")

conn = sqlite3.connect("sql_test.db")

data.to_sql(
            'airport',             # Name of the sql table
            conn,                 # sqlite.Connection or sqlalchemy.engine.Engine
            if_exists='replace'
           )


cursor = conn.cursor()
cursor.execute("""SELECT Date, AirportName, PercentOfBaseline  
                  FROM airport
                  LIMIT 5""")
result = cursor.fetchall()
if result:
    print(result)
pass
#sqlite_master