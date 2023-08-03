# Pandas to MySQL Bulk Insert Method Comparison

## Method 1: mysql.connector
Python library used to connect and interact with MySQL databases. It provides a convenient interface to execute SQL queries and manage connections to a MySQL database from Python code. This method connects directly to sql database and itterates through rows in pandas df inserting into table one at a time.

## Method 2: SQLalchemy
Provides an Object-Relational Mapping (ORM) system that allows you to interact with a database using Python classes and objects instead of raw SQL queries and so doesnt have to itterate through df rows. 

## Method 3: SQLalchemy + pymysql
When you set fast_executemany to True with pymysql, pymysql optimizes the bulk insert or update operation by batching the SQL queries together and sending them as a single multi-row query to the database server.

## Results
To test the speed and efficiency of each method a sample pandas df is created containing 5 columns for each row (random 10 character string, random integer between 1000 and 9999, random float number between 10 and 99, random boolean in integer form, random date between 2010 and 2020.)


Running on Razer blade 15 2020 laptop average run times over 10 test runs 

| Rows    | mysql.connector (s)  | sqlalchemy (s) | sqlalchemy + pymysql (s) |
| :---:   |        :---:         |      :---:     |          :---:           |
| 100     |        0.11          |      0.11      |          0.06            |
| 1000    |        0.57          |      0.09      |          0.03            |
| 10000   |        5.53          |      0.39      |          0.22            |
| 100000  |        50.50         |      2.74      |          1.94            |
| 250000  |        127.09        |      6.78      |          4.79            |
| 500000  |        258.68        |      13.82     |          9.60            |
| 1000000 |        520.10        |      28.36     |          19.60           |

##

![figure](https://github.com/adamcorren/pandas_to_mysql_optimisation/assets/125222047/f30c04af-d531-455f-a3a7-ce43c589e1fa)
