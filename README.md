# Welcome to Sparkify!

The objective of this project is to practice skills in Data Modeling with Postgres


## Files and descriptions
|           File                |        Description          |
|-------------------------------|-----------------------------|
|`sql_queries.py `              |All query need to create, drop and insert        |
|`create_tables.py `            |File that call sql_queries to create the database|
|`etl.py`                       |All ETL procesc                                  |
|`etl.ipynb`                    |ETL explanation                                  |
|`test.ipynb`                   |Testing file                                     |

# ETL process and ER Diagram

Now let's see Sparkify's ER Diagram and ETL process. After understand the diagram, all function to perform the ETL process will be explained. 

## ER Diagram
---
![Sparkify ER Diagram](https://i.postimg.cc/wvg9Khsc/ERD.jpg)

## ETL process
---
### All fuction inside file etl.py
|      Function      |        Description                      |
|--------------------|-----------------------------------------|
|`main`              |Create connection and call `process_data`|
|`process_data `     |Process all files from specific folder   |
|`process_song_file` |Process all ETL steps to song files      |
|`process_log_file`  |Process all ETL steps to log files       |



# Running the python scripts
First of all we must make sure that two dependencies exist:
  1. Creating a studentdb database <br>
  `CREATE DATABASE studentdb;`
  2. Creating a student user <br>
  `CREATE USER student WITH PASSWORD 'student';`


then we must run the `create_tables.py` file and then the `etl.py` file.