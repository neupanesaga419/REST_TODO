### Todo CRUD usign Django Rest

## This Application is made using Django Rest as backend to handle api and for db
## SQLITE is used.

This site contains a table with name Todo having four fields
"title", "description","is_completed"

this contains four urls:


localhost:8000/api/get_todo/  -> this handles only GET method. Helps in getting 
all the todos present in database.
We can retrive the data using filter in accordance to is_completed:

to filter data one need to enter url 
localhost:8000/api/get_todo/?completed=True
localhost:8000/api/get_todo/?completed=False

######  ---------------------------------------------



localhost:8000/api/create_todo/ -> this handles only POST method. 
This url helps to insert the data into the db.

##### ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>------------------

localhost:8000/api/update_todo/id
this url takes three http methods GET,POST and PUT
1. GET for retrieveing the requested data with id.
2. POST for updating all the values:
3. PUT for updating partial values: 

#### -----------------------------------------------------------
localhost:8000/api/delete_todo/id

this url takes only one HTTP method Delete.
This url helps to delete the data present in the database with its id.
