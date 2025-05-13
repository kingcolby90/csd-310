#Colby king module 6.2 assignment#
import mysql.connector
from dotenv import dotenv_values

secrets = dotenv_values(".env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print(f"Connected to MySQL database {config['database']}!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    db.close()