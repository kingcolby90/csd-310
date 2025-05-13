#movies_queries
#colby king module 7 assignment#
import mysql.connector
from dotenv import dotenv_values

# Load credentials from the .env file
secrets = dotenv_values(".env")

# Database configuration
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

# Establish connection to the MySQL database
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    query1 = "SELECT studio_id, studio_name FROM studio"
    cursor.execute(query1)
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

    # Query 2: Select all fields from the genre table
    query2 = "SELECT genre_id, genre_name FROM genre"
    cursor.execute(query2)
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

    # Query 3: Select movies with a runtime of less than two hours (120 minutes)
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query3)
    short_films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print(f"Film Name: {film[0]}\nRuntime: {film[1]}\n")

    # Query 4: Select film names and directors, grouped by director
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director"
    cursor.execute(query4)
    directors = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for record in directors:
        print(f"Film Name: {record[0]}\nDirector: {record[1]}\n")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    db.close()