# FlaskMySQLStarterProj
## A Starter Project to Utilize MySQL and Flask Together

## TITLE : ATTENDANCE MANAGEMENT SYSTEM

This is an starter/entry level project developed in the process of trying out working with MySQL and Flask. At the point of writing this documentation, the project is in a barebones state. I plan to add more feature additions as and when I get the time.

Firstly, the database consists of three tables namely:

1. student : Table with student data (Student ID, associated Teacher ID, Student Name, Class, and Section)
2. teacher : Table with teacher data (Teacher ID, Teacher Name, Course taught)
3. attendance : Table with Student ID, Teacher ID, Date of attendance, Status of attendance (Present - P, or Absent - A)

Currently, the application enables the user to:
1. add data to the student, teacher tables,
2. add attendance data for an associated Student ID, Teacher ID, date, and attendance status (P/A),
3. retrieve attendance list for given date input, and 
4. lastly the user can enter an SQL query as an input and is given the result/output for the Query given as input.

  At the point of writing this documentation, the application only caters basic functions and features, though I plan to add more plausible actions/interactions with the data with probable addition of other possible CRUD operations, UI changes, etc.

## LEARNING RESOURCE UTILIZED
I would like to share that the major credit for successful completion of this project (though a starter proj) goes to this excellent tutorial video of how to work with Flask and MySQL DBMS linked here : https://www.youtube.com/watch?v=6L3HNyXEais

## CLONE INSTRUCTIONS
If for whatever reason, the reader wanted to clone this repo locally and tinker with the code there are few pre-requisite steps to be followed:

### 1. Firstly create a Virtual Environment and install packages
For creating the virtual environment, open your terminal (or command line incase of Windows) and run the following command:

`python3 -m venv /path/to/new/virtual/environment`

After you succesfully create the virtual environment, for installing the packages, dependencies mentioned in the requirements.txt file follow the steps:
1. Activate the virtual environment by entering the command:

`(name_of_virt_environ)\Scripts\activate`

2. Now execute the following command to install all the dependencies at once:

`pip install -r /path/to/requirements.txt`

### 2. Adding MySQL database config details

For running the application, we require the details such as MySQL HOST, User, Password, and the Database. These details are to be stored in a separate file named `db.yaml` (not strictly the same, but if you wish to change the name of file, changes in code are needed). For this you can refer to the above mentioned video tutorial for clear instructions.
