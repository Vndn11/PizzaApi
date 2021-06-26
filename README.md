##### PizzaApi #####

***** How to Run Project *****
1.DOWNLOAD
2.INSTALLATION 
3.EXECUTE



- Download and Install Following Softwares :
    + Python == https://www.python.org/downloads/release/python-395/
    + Mongodb Community Server == https://www.mongodb.com/try/download/community
    + Visual Studio Code == https://code.visualstudio.com/download


- Install Packages :
    + Open Command Prompt (Folder where 'Requirement.txt' is located)
    + Activate your virtualenv
    + Run command == 'pip install -r requirements.txt'


- Execute the project using following steps:
    + Download and Extract Project file 
    + Open Mongodb Compass and create new database 'Pizza'
    + Open project folder in Visual Studio Code
    + Open new terminal 
    + Run command == python manage.py makemigrations
                  == python manage.py migrate
                  == python manage.py runserver
    + Open Browser and search for == localhost:8000/api/  ('8000' may vary)
    + Run different API's using given urls
 
 
 - API's :
    + localhost:8000/api/ == Lists all the stored Pizza in the Database, also list its size and type along with toppings.
    + localhost:8000/api/<size_id> == List all the stored Pizza of given size.
    + localhost:8000/api/<type_id> == List all the stored Pizza of given type.
    + localhost:8000/api/create == Create a new pizza in database.
    + localhost:8000/api/edit/<pizza_id> == Edit the given stored Pizza information in database.
    + localhost:8000/api/delete/<pizza_id> == Deletes the given stored Pizza from database.





