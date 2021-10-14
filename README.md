# fastapi-postgresql-app
\
REST-service with 3 endpoints

1. get JSON {id, value} request, parse data and put in DB.
2. return data from the DB with filters by fields and LIMIT and OFFSET parameters.
3. get JSON {id, value} request and update value found by id. If there is no such id return error.



Columns in the DB: id(int), value(str), timestamp(int)



```
To launch:
pip3 install -r requirements.txt
uvicorn db_app.main:app
```
