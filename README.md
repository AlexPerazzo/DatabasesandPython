# Overview

The purpose of this program is to give me practice integrating mySQL/databases in general with code (python in particular in this case). I think Databases are a super important tool, and I want to get more comfortable using them.

In this case, it's a straight forward to-do list style of code, but everything is saved/drawn from a database using mySQL. Feel free to take a look at this video where I explain the code more in depth.

[Software Demo Video](https://youtu.be/XMdEDJzrZEo)

# The Database

I am using mySQL, with a server running through MySQL workbench 8.0. I create a new database (if it doesn't exist already) with a table that has a auto_incrementing key and a column of characters.

# Development Environment

Visual Studio Code is the IDE I used. The code is in python and I had to import mysql.connector.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [W3 Schools](https://www.w3schools.com/mysql/mysql_sql.asp)
- [YouTube: Python and MySQL - Populating our Database and Table](https://www.youtube.com/watch?v=BfXhZDNlXy8)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Allow the user to create their own columns (more details they want stored about the movie)
- Catches if movie already exists when adding a movie
- Catches if movie doesn't exist when trying to delete
