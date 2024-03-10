import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()


mycursor.execute("SHOW DATABASES")
list_of_dbs = []
for db in mycursor:
    list_of_dbs.append(db)
print(list_of_dbs)

if ('to_watch_movies',) not in list_of_dbs:
    
    mycursor.execute("CREATE DATABASE to_watch_movies")
    mycursor.execute("USE to_watch_movies")
    sql = """
    CREATE TABLE movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255)
    )
    """
    mycursor.execute(sql)

else:
    mycursor.execute("USE to_watch_movies")

print("Welcome to your Movie To-Watch List!")
response = -1
while response != 4:
    print("Would you like to 1. Add a movie, 2. Mark a movie as watched, 3. View the List, or 4. Quit?")

    response = int(input())

    if response == 1:
        print("What would you like to add?")
        add_this = input()
        sql = "INSERT INTO movies (title) VALUES (%s)"
        mycursor.execute(sql, (add_this,))
        print(f"{add_this} was added.")

    elif response == 2:
        print("What would you like to delete?")
        delete_this = input()
        sql = "DELETE FROM movies WHERE title = (%s)"
        mycursor.execute(sql, (delete_this,))

    elif response == 3:
        sql = "SELECT title FROM movies"
        mycursor.execute(sql)
        titles = mycursor.fetchall()

        for title in titles:
            print(title)

    elif response == 4:
        print("Goodbye!")
    else:
        print("Invalid input, please try again.")






mydb.commit()
mydb.close()
mycursor.close()