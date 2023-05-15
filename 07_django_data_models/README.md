https://docs.djangoproject.com/en/4.0/intro/tutorial02/

# Object Relational Mapping ORM
- Allow us to map tables to objects and columns
- use those obj to srore and retrieve data from db
- improved portablility across db dialects-mutiple dbs


- The makemigrations command reads all the models.py files in all the applications, end create/evolves the migration files
- Guided by the applications listed in settings.py
- Migrations are portable across databases

- The migrate command reads all the migrations folders in the application folders and create/ evolves the tables in the database(i.e. db.sqlite3)

## Re-running makemigration

- delete 0001_initial.py all thoes files
- then re run the makemigration

another way is delete db.sqllit3 and do migrate from scratch. but we'll lose all data
```
python3 manage.py makemigrations
```