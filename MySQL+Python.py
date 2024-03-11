import mysql.connector

def main():
    
    mycursor, mydb = connect_to_database()
    create_if_first_run(mycursor)

    print("Welcome to your Movie To-Watch List!")
    response = -1
    while response != 6:
        print("Would you like to 1. Add a movie, 2. Mark a movie as watched, 3. View the List, 4. View Watched List, 5. Rate a Watched Movie, or 6. Quit?")

        response = int(input())

        if response == 1:
            print("What would you like to add?")
            add_this = input()

            if it_exists(mycursor, add_this, "movies"):
                print("That already exists in your list!")

            else:
                sql = "INSERT INTO movies (title) VALUES (%s)"
                mycursor.execute(sql, (add_this,))
                print(f"{add_this} was added.")

        elif response == 2:
            print("What would you like to mark as watched?")
            delete_this = input()
            
            if it_exists(mycursor, delete_this, "movies"):

                sql = "DELETE FROM movies WHERE title = (%s)"
                mycursor.execute(sql, (delete_this,))
                sql = "INSERT INTO watched_movies (title) VALUES (%s)"
                mycursor.execute(sql, (delete_this,))
                print(f"{delete_this} has been marked as watched.")
                
            else:
                print("That does not exist in your list!")

        elif response == 3:
            sql = "SELECT title FROM movies"
            mycursor.execute(sql)
            titles = mycursor.fetchall()

            for title in titles:
                print(title)

        elif response == 4:
            sql = "SELECT title, rating FROM watched_movies"
            mycursor.execute(sql)
            titles = mycursor.fetchall()

            for title in titles:
                print(title)

        elif response == 5:
            print("Which watched movie would you like to give a rating?")
            rate_this = input()
            
            if it_exists(mycursor, rate_this, "watched_movies"):
                print("What rating would you like to give this movie?")
                rating = input()
                sql = "UPDATE watched_movies SET rating = (%s) WHERE title = (%s)"
                mycursor.execute(sql, (rating, rate_this))
                print(f"{rate_this} has been given the rating of {rating}.")
                
            else:
                print("That does not exist in your watched movies list!")


        elif response == 6:
            print("Goodbye!")

        else:
            print("Invalid input, please try again.")


    mydb.commit()
    mydb.close()
    mycursor.close()

def create_if_first_run(mycursor):
    mycursor.execute("SHOW DATABASES")
    list_of_dbs = []
    for db in mycursor:
        list_of_dbs.append(db)
    
    if ('to_watch_movies',) not in list_of_dbs:
            
            mycursor.execute("CREATE DATABASE to_watch_movies")
            mycursor.execute("USE to_watch_movies")
            sql = """
            CREATE TABLE movies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255)
                
            );
            CREATE TABLE watched_movies (
                watched_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                rating VARCHAR(255)
            )
            """
            mycursor.execute(sql)

    else:
        mycursor.execute("USE to_watch_movies")

def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    mycursor = mydb.cursor()
    return mycursor, mydb

def it_exists(mycursor, thing, location):
    sql = f"SELECT * FROM {location} WHERE title = %s"
    mycursor.execute(sql, (thing,))
    result = mycursor.fetchone()
    if result:
        return True
    else:
        return False

def reset_database(mycursor):
    this_one = "to_watch_movies"
    sql = "DROP DATABASE IF EXISTS " + this_one
    mycursor.execute(sql)

main()