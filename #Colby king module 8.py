#Colby king module 8.2 assignment#
import mysql.connector

def show_films(cursor, title):
    print(f"\n{title}\n" + "-"*50)
    
    query = """
    SELECT 
        film.film_name AS Name, 
        film.film_director AS Director,
        genre.genre_name AS Genre, 
        studio.studio_name AS Studio
    FROM film 
    INNER JOIN genre ON film.genre_id = genre.genre_id 
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    
    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print(f"Name: {film[0]}, Director: {film[1]}, Genre: {film[2]}, Studio: {film[3]}")

# Establishing Connection to Movies Database
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="movies"
)
cursor = conn.cursor()

# Call `show_films` Function to Display Initial Data
show_films(cursor, "DISPLAYING FILMS")

# **Insert a New Film Record**
cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id) VALUES ('Inception', 'Christopher Nolan', 1, 2)")
conn.commit()

# **Display Films After Insertion**
show_films(cursor, "AFTER INSERTING NEW FILM")

# **Update Alien's Genre to Horror**
cursor.execute("UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'")
conn.commit()

# **Display Films After Update**
show_films(cursor, "AFTER UPDATING 'ALIEN' TO HORROR")

# **Delete Gladiator from the Database**
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
conn.commit()

# **Display Films After Deletion**
show_films(cursor, "AFTER DELETING 'GLADIATOR'")

# Close Database Connection
cursor.close()
conn.close()