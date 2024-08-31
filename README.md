# Linux_db_backup_automation



raw instructions by himanshu for linux db backup automation=>

install wsl via powershell admin mode (wsl --install). once installed install mysql as well in wsl cli.
now let's create a db backup automation function here:

1st login to mysql create a new database: create database new_db
then create a table: CREATE TABLE user_data (
   			 id INT AUTO_INCREMENT PRIMARY KEY,
   			 name VARCHAR(100),
  			  email VARCHAR(100)
			 );
once table is created cross check it by: show tables;
now let's create a python function to input the user data on table:
1st check if we have mysql connector for python if not then install: pip install mysql-connector-python
now let's write the python script to insert the data: nano input_data.py:
now run the python script and cross check the datbase that data is inserted or not. (note: we have to create a function where we take data and store on the database "new_db")

now lets write a backup script and run it by giving executable permission and check for the .sql file, that is your back up.
restore it to a new database and cross check the details if any mismatch or anyhting. 
